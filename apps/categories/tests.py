import sympy as sp


def calculate_cutting_force_differential_exponent():
    Cp, t, xp, Sz, yp, B, z, D, qp = sp.symbols('Cp t xp Sz yp B z D qp')

    Pz = (9.81 * Cp * t ** xp * Sz ** yp * B * z) / D ** qp

    dPz_dxp = sp.diff(Pz, xp)
    dPz_dyp = sp.diff(Pz, yp)
    dPz_dqp = sp.diff(Pz, qp)

    return dPz_dxp, dPz_dyp, dPz_dqp


def main():
    print("Kesish kuchi Pz ning xp, yp va qp daraja ko'rsatkichlari bo'yicha differensial tenglamalari:\n")

    dPz_dxp, dPz_dyp, dPz_dqp = calculate_cutting_force_differential_exponent()

    print(f"dPz/dxp = {dPz_dxp}")
    print(f"dPz/dyp = {dPz_dyp}")
    print(f"dPz/dqp = {dPz_dqp}")


if __name__ == "__main__":
    main()

