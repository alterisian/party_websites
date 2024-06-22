
document.addEventListener("DOMContentLoaded", function() {
    const policies = ["Have defense supplies handled by government run companies, so there is less profit incentive for war.", "Have a vote on real Proportional Representation (PR), since the last vote was AV.", "Increase funding for public education.", "Reduce carbon emissions by 50% by 2030.", "Increase the minimum wage to £15 per hour.", "Provide affordable housing for all citizens.", "Ensure free college tuition for all students.", "Increase funding for mental health services.", "Support small businesses through grants and tax incentives.", "Expand public transportation infrastructure.", "Promote gender equality in the workplace.", "Promote renewable energy job training programs.", "Increase funding for scientific research and development.", "Implement stricter regulations on pollution and waste.", "Promote local and sustainable agriculture.", "Expand access to childcare services.", "Improve infrastructure in rural areas.", "Increase public safety through community policing.", "Enhance arts and culture funding.", "Promote digital literacy and access to technology.", "Ensure fair and transparent elections.", "Increase transparency and accountability in government.", "Reduce student loan debt.", "Support renewable energy initiatives.", "Protect wildlife and natural habitats.", "Promote public health and wellness programs.", "Enhance educational resources for teachers and students.", "Reduce inequality through a wealth tax"];
    const policyTextElement = document.getElementById("policy-text");
    const newPolicyButton = document.getElementById("new-policy-button");

    function setRandomPolicy() {
        const randomPolicy = policies[Math.floor(Math.random() * policies.length)];
        policyTextElement.textContent = randomPolicy;
    }

    newPolicyButton.addEventListener("click", setRandomPolicy);

    // Set initial random policy
    setRandomPolicy();
});
