from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Estrutura do grafo
model = BayesianModel([
    ('Qualidade', 'Falha'),
    ('Falha', 'Atraso'),
    ('Atraso', 'Custo')
])

# CPDs
cpd_qualidade = TabularCPD(variable='Qualidade', variable_card=2, values=[[0.7], [0.3]])  # 0 = Alta, 1 = Baixa

cpd_falha = TabularCPD(
    variable='Falha', variable_card=2,
    values=[[0.9, 0.2], [0.1, 0.8]],  # 0 = Não, 1 = Sim
    evidence=['Qualidade'], evidence_card=[2]
)

cpd_atraso = TabularCPD(
    variable='Atraso', variable_card=2,
    values=[[0.8, 0.25], [0.2, 0.75]],  # 0 = Não, 1 = Sim
    evidence=['Falha'], evidence_card=[2]
)

cpd_custo = TabularCPD(
    variable='Custo', variable_card=2,
    values=[[0.8, 0.15], [0.2, 0.85]],  # 0 = Não, 1 = Sim
    evidence=['Atraso'], evidence_card=[2]
)

# Adiciona os CPDs ao modelo
model.add_cpds(cpd_qualidade, cpd_falha, cpd_atraso, cpd_custo)

# Verifica se é válido
assert model.check_model()

# Inferência
infer = VariableElimination(model)

# Exemplo: Qual a probabilidade de aumento de custo se a qualidade for baixa?
resultado = infer.query(variables=['Custo'], evidence={'Qualidade': 1})
print(resultado)
