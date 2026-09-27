import time
import pandas as pd
import streamlit as st

# ==========================================
# 1. ACCESSIBILITY & STYLING CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Nostrix Charity - Empowering Lives",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for high contrast, warm earth tones, responsive cards, and large CTAs
st.markdown(
    """
    <style>
    /* Warm, inviting color palette & WCAG 2.1 contrast standards */
    .stApp {
        background-color: #f9fbf9;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        color: #1c2e24;
    }
    
    /* Prominent CTA Buttons */
    .stButton>button {
        background-color: #2e6f40;
        color: #ffffff;
        font-size: 1.1rem;
        font-weight: 700;
        border-radius: 8px;
        min-height: 52px;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #21512e;
        color: #ffffff;
        transform: translateY(-1px);
    }

    /* Visual Hierarchy Cards */
    .hero-card {
        background-color: #eaf2eb;
        border-left: 6px solid #2e6f40;
        padding: 24px;
        border-radius: 8px;
        margin-bottom: 24px;
    }
    .story-card {
        background-color: #ffffff;
        border: 1px solid #dcdcdc;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 16px;
    }
    .trust-badge {
        background-color: #1c2e24;
        color: #ffffff;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-block;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ==========================================
# 2. SESSION STATE MANAGEMENT
# ==========================================
if "total_raised" not in st.session_state:
    st.session_state.total_raised = 68500
if "goal_amount" not in st.session_state:
    st.session_state.goal_amount = 100000
if "volunteer_hours" not in st.session_state:
    st.session_state.volunteer_hours = 1240
if "donations_count" not in st.session_state:
    st.session_state.donations_count = 842

# ==========================================
# 3. NAVIGATION & ACCESSIBLE SIDEBAR
# ==========================================
st.sidebar.title("🌿 Nostrix Charity")
st.sidebar.markdown(
    '<span class="trust-badge">⭐ Charity Navigator 4-Star Rated</span>',
    unsafe_allow_html=True,
)
st.sidebar.markdown("---")

# Navigation Menu
nav_selection = st.sidebar.radio(
    "Navigation Menu",
    [
        "Home",
        "Donate Now",
        "Impact Stories",
        "Volunteer",
        "Financial Transparency",
    ],
    label_visibility="collapsed",
)

st.sidebar.markdown("---")
st.sidebar.caption("🔒 **100% Encrypted & Secure Payments**")
st.sidebar.caption("♿ WCAG 2.1 AAA Compliant Mode")


# ==========================================
# 4. PAGE: HOMEPAGE
# ==========================================
if nav_selection == "Home":
    # Hero Section
    st.markdown(
        """
        <div class="hero-card">
            <h1 style="color: #2e6f40; margin-bottom: 8px;">Help 100 Children in Need Today</h1>
            <p style="font-size: 1.25rem; line-height: 1.5;">
                Nostrix Charity delivers clean water, nutritious meals, and education directly to underfunded communities worldwide. Every single contribution creates a lasting impact.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Call-to-Action & Real-time Progress Bar
    st.subheader("Current Campaign: Child Nutrition Initiative")
    progress_percentage = min(
        1.0, st.session_state.total_raised / st.session_state.goal_amount
    )
    st.progress(progress_percentage)

    stat_col1, stat_col2, stat_col3 = st.columns(3)
    stat_col1.metric(
        "Raised So Far", f"${st.session_state.total_raised:,.2f}"
    )
    stat_col2.metric("Campaign Goal", f"${st.session_state.goal_amount:,.2f}")
    stat_col3.metric("Total Donors", f"{st.session_state.donations_count:,}")

    st.markdown("---")

    # Quick Impact Banner
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.subheader("Why Support Nostrix?")
        st.write(
            "• **100% Transparency:** 85% of funds go straight to field operations.\n"
            "• **Direct Impact:** Over 12,000 meals distributed this year alone.\n"
            "• **Community Driven:** Powered by local volunteers and global donors."
        )
    with col_b:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("❤️ Donate Now to This Cause", use_container_width=True):
            st.info("Please navigate to the 'Donate Now' tab in the menu to complete your contribution!")

    st.markdown("---")

    # Highlighting Stories
    st.subheader("Featured Beneficiary Stories")
    s_col1, s_col2 = st.columns(2)
    with s_col1:
        st.markdown(
            """
            <div class="story-card">
                <h3>Amina's Journey to School</h3>
                <p><em>"Receiving daily lunches allowed me to stay in school and prepare for my exams without worrying about hunger."</em></p>
                <p><strong>Impact:</strong> Provided 6 months of educational support and meals.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with s_col2:
        st.markdown(
            """
            <div class="story-card">
                <h3>Clean Water in Village Hope</h3>
                <p><em>"Our community now has access to safe drinking water right near our homes, improving overall health."</em></p>
                <p><strong>Impact:</strong> Built a sustainable solar-powered water well.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ==========================================
# 5. PAGE: DONATION SECTION
# ==========================================
elif nav_selection == "Donate Now":
    st.header("Make a Secure Donation")
    st.caption("Guide through simple steps to make an immediate impact.")

    # Step-by-Step Flow
    st.subheader("Step 1: Select Your Contribution")

    donation_type = st.radio(
        "Donation Frequency",
        ["One-Time Gift", "Monthly Giving (Recommended)"],
        horizontal=True,
    )

    preset_amount = st.radio(
        "Select Amount (USD)",
        ["$25", "$50", "$100", "$250", "Custom Amount"],
        horizontal=True,
    )

    if preset_amount == "Custom Amount":
        custom_val = st.number_input(
            "Enter Custom Amount ($)", min_value=1.0, value=75.0, step=5.0
        )
        final_amount = custom_val
    else:
        final_amount = float(preset_amount.replace("$", ""))

    st.markdown("---")
    st.subheader("Step 2: How Your Gift Helps")

    # Dynamic visual impact breakdown based on selected amount
    meals_provided = int(final_amount * 2)
    kits_provided = int(final_amount / 25)

    st.success(
        f"Your donation of **${final_amount:.2f}** can provide approximately **{meals_provided} nutritious meals** or **{kits_provided} school supply kits** to children in need!"
    )

    st.markdown("---")
    st.subheader("Step 3: Payment Details")

    with st.form("donation_form"):
        f_name = st.text_input("Full Name", placeholder="Jane Doe")
        f_email = st.text_input("Email Address (for receipt)", placeholder="jane@example.com")
        pay_gateway = st.selectbox(
            "Payment Gateway", ["Stripe (Credit/Debit)", "PayPal", "Apple Pay / Google Pay"]
        )

        st.caption("🔒 All transactions are secured using 256-bit SSL encryption.")

        submit_donation = st.form_submit_button("Complete Donation")

        if submit_donation:
            if not f_name or not f_email:
                st.error("Please fill in your name and email address.")
            else:
                # Update State
                st.session_state.total_raised += final_amount
                st.session_state.donations_count += 1

                st.balloons()
                st.success(f"Thank you, {f_name}! Your {donation_type.lower()} of ${final_amount:.2f} via {pay_gateway} was successful.")
                st.info(f"A tax-deductible receipt has been dispatched to {f_email}.")


# ==========================================
# 6. PAGE: IMPACT STORIES & GALLERY
# ==========================================
elif nav_selection == "Impact Stories":
    st.header("Real-Life Impact Stories")
    st.caption("See how donor contributions translate into real-world transformations.")

    search_term = st.text_input("🔍 Search stories by keyword or region:", "")

    stories_data = [
        {
            "title": "Clean Water Initiative",
            "region": "Sub-Saharan Africa",
            "text": "Over 500 families now have access to clean, reliable water sources, reducing waterborne illness by 75%.",
            "tag": "Health",
        },
        {
            "title": "Emergency Meal Distribution",
            "region": "Southeast Asia",
            "text": "Nutritional kits distributed to emergency shelters following severe seasonal flooding.",
            "tag": "Relief",
        },
        {
            "title": "Youth Literacy & Books",
            "region": "South America",
            "text": "Built two community libraries stocked with over 1,500 books and learning materials.",
            "tag": "Education",
        },
    ]

    filtered_stories = [
        s for s in stories_data
        if search_term.lower() in s["title"].lower() or search_term.lower() in s["text"].lower() or search_term.lower() in s["tag"].lower()
    ]

    for st_item in filtered_stories:
        st.markdown(
            f"""
            <div class="story-card">
                <span class="trust-badge">{st_item['tag']}</span>
                <h3 style="margin-top: 8px;">{st_item['title']} ({st_item['region']})</h3>
                <p>{st_item['text']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ==========================================
# 7. PAGE: VOLUNTEER & ENGAGEMENT
# ==========================================
elif nav_selection == "Volunteer":
    st.header("Join as a Volunteer")
    st.caption("Your time and expertise can change lives directly.")

    v_col1, v_col2 = st.columns([2, 1])

    with v_col1:
        st.subheader("Volunteer Registration Form")
        with st.form("volunteer_form"):
            v_name = st.text_input("Name")
            v_email = st.text_input("Email")
            v_role = st.selectbox(
                "Preferred Role",
                [
                    "Community Meal Distribution",
                    "Event Coordination",
                    "Remote Marketing & Design",
                    "Fundraising Ambassador",
                ],
            )
            v_hours = st.slider("Weekly Availability (Hours)", 1, 20, 5)

            v_submit = st.form_submit_button("Submit Application")

            if v_submit:
                if v_name and v_email:
                    st.session_state.volunteer_hours += v_hours
                    st.success(f"Thank you, {v_name}! We have received your application for {v_role}.")
                else:
                    st.error("Please provide both name and email.")

    with v_col2:
        st.subheader("Community Impact")
        st.metric("Total Volunteer Hours Logged", f"{st.session_state.volunteer_hours:,} hrs")

        st.markdown(
            """
            <div class="hero-card" style="margin-top: 10px;">
                <h4>Impact Conversion</h4>
                <p>• <strong>10 Vol. Hours</strong> = 50 Meals Served</p>
                <p>• <strong>50 Vol. Hours</strong> = 1 Well Maintained</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ==========================================
# 8. PAGE: FINANCIAL TRANSPARENCY
# ==========================================
elif nav_selection == "Financial Transparency":
    st.header("Financial Transparency & Trust")
    st.caption("We believe donors deserve total clarity on where every dollar goes.")

    st.subheader("How Your Donation Is Allocated")

    # Allocation Data Chart
    financial_data = pd.DataFrame(
        {
            "Category": [
                "Direct Program Services",
                "Administrative & Operations",
                "Fundraising & Awareness",
            ],
            "Percentage": [85, 10, 5],
        }
    )

    st.dataframe(
        financial_data,
        column_config={
            "Category": "Budget Category",
            "Percentage": st.column_config.NumberColumn("Percentage Allocation", format="%d%%"),
        },
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("---")
    st.subheader("Accreditations & Badges")
    badge_col1, badge_col2, badge_col3 = st.columns(3)
    badge_col1.info("🏅 **Charity Navigator**\n\n4/4 Stars (100% Score)")
    badge_col2.info("🛡️ **BBB Accredited**\n\nMeets all 20 Standards")
    badge_col3.info("✅ **GuideStar Gold**\n\nTransparency Seal")


# ==========================================
# 9. FOOTER (ACCESSIBLE & TRANSPARENT)
# ==========================================
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns(3)
with footer_col1:
    st.caption("© 2026 Nostrix Charity. All rights reserved.")
with footer_col2:
    st.caption("[Privacy Policy](#) | [Terms of Service](#) | [Accessibility Statement](#)")
with footer_col3:
    st.caption("Contact: support@nostrixcharity.org | +1 (800) 555-0199")