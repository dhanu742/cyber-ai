from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from datetime import datetime


# =========================
# GENERATE PDF REPORT
# =========================

def generate_report(

    data,
    prediction,
    score,
    attack_type,
    reasons

):

    filename = "enterprise_security_report.pdf"

    doc = SimpleDocTemplate(
        filename
    )

    styles = getSampleStyleSheet()

    content = []


    # =====================
    # TITLE
    # =====================

    content.append(

        Paragraph(

            "ENTERPRISE CYBER SECURITY REPORT",

            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )


    # =====================
    # DATE
    # =====================

    content.append(

        Paragraph(

            f"""
            <b>Generated:</b>
            {datetime.now()}
            """,

            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 10)
    )


    # =====================
    # PREDICTION
    # =====================

    content.append(

        Paragraph(

            f"""
            <b>Prediction:</b>
            {prediction}
            """,

            styles["Normal"]
        )
    )


    # =====================
    # ATTACK TYPE
    # =====================

    content.append(

        Paragraph(

            f"""
            <b>Attack Type:</b>
            {attack_type}
            """,

            styles["Normal"]
        )
    )


    # =====================
    # RISK SCORE
    # =====================

    content.append(

        Paragraph(

            f"""
            <b>Risk Score:</b>
            {score}%
            """,

            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 20)
    )


    # =====================
    # THREAT ANALYSIS
    # =====================

    content.append(

        Paragraph(

            "Threat Analysis",

            styles["Heading2"]
        )
    )

    for reason in reasons:

        content.append(

            Paragraph(

                reason,

                styles["Normal"]
            )
        )

    content.append(
        Spacer(1, 20)
    )


    # =====================
    # SECURITY RECOMMENDATIONS
    # =====================

    content.append(

        Paragraph(

            "Security Recommendations",

            styles["Heading2"]
        )
    )

    recommendations = """

    - Avoid suspicious links

    - Verify domains carefully

    - Enable MFA / 2FA

    - Use antivirus protection

    - Avoid unknown redirects

    - Keep systems updated

    - Train users against phishing

    """

    content.append(

        Paragraph(

            recommendations,

            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 20)
    )


    # =====================
    # ENTERPRISE SUMMARY
    # =====================

    summary = f"""

    This analysis identified
    a potential security threat
    categorized as:

    <b>{attack_type}</b>

    with a calculated
    enterprise risk score of:

    <b>{score}%</b>

    """

    content.append(

        Paragraph(

            summary,

            styles["Normal"]
        )
    )


    # =====================
    # BUILD PDF
    # =====================

    doc.build(content)

    return filename