_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
siemens,=mibBuilder.importSymbols('SIEMENS-SMI','siemens')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
automation=ModuleIdentity((1,3,6,1,4,1,4329,6))
if mibBuilder.loadTexts:automation.setRevisions(('2013-06-25 00:00','2012-07-27 00:00','2008-11-10 00:00','2008-06-02 00:00','2008-04-29 00:00','2005-01-12 00:00'))
_AutomationProducts_ObjectIdentity=ObjectIdentity
automationProducts=_AutomationProducts_ObjectIdentity((1,3,6,1,4,1,4329,6,1))
if mibBuilder.loadTexts:automationProducts.setStatus(_A)
_AutomationPlc_ObjectIdentity=ObjectIdentity
automationPlc=_AutomationPlc_ObjectIdentity((1,3,6,1,4,1,4329,6,1,1))
if mibBuilder.loadTexts:automationPlc.setStatus(_A)
_AutomationSimaticNet_ObjectIdentity=ObjectIdentity
automationSimaticNet=_AutomationSimaticNet_ObjectIdentity((1,3,6,1,4,1,4329,6,1,2))
if mibBuilder.loadTexts:automationSimaticNet.setStatus(_A)
_AutomationMotionControl_ObjectIdentity=ObjectIdentity
automationMotionControl=_AutomationMotionControl_ObjectIdentity((1,3,6,1,4,1,4329,6,1,3))
if mibBuilder.loadTexts:automationMotionControl.setStatus(_A)
_AutomationHmi_ObjectIdentity=ObjectIdentity
automationHmi=_AutomationHmi_ObjectIdentity((1,3,6,1,4,1,4329,6,1,4))
if mibBuilder.loadTexts:automationHmi.setStatus(_A)
_AutomationSitopPower_ObjectIdentity=ObjectIdentity
automationSitopPower=_AutomationSitopPower_ObjectIdentity((1,3,6,1,4,1,4329,6,1,5))
if mibBuilder.loadTexts:automationSitopPower.setStatus(_A)
_AutomationModules_ObjectIdentity=ObjectIdentity
automationModules=_AutomationModules_ObjectIdentity((1,3,6,1,4,1,4329,6,2))
if mibBuilder.loadTexts:automationModules.setStatus(_A)
_AutomationMgmt_ObjectIdentity=ObjectIdentity
automationMgmt=_AutomationMgmt_ObjectIdentity((1,3,6,1,4,1,4329,6,3))
if mibBuilder.loadTexts:automationMgmt.setStatus(_A)
_AutomationAgentCapability_ObjectIdentity=ObjectIdentity
automationAgentCapability=_AutomationAgentCapability_ObjectIdentity((1,3,6,1,4,1,4329,6,4))
if mibBuilder.loadTexts:automationAgentCapability.setStatus(_A)
_AutomationPlcAgentCapability_ObjectIdentity=ObjectIdentity
automationPlcAgentCapability=_AutomationPlcAgentCapability_ObjectIdentity((1,3,6,1,4,1,4329,6,4,1))
if mibBuilder.loadTexts:automationPlcAgentCapability.setStatus(_A)
_AutomationSimaticNetAgentCapability_ObjectIdentity=ObjectIdentity
automationSimaticNetAgentCapability=_AutomationSimaticNetAgentCapability_ObjectIdentity((1,3,6,1,4,1,4329,6,4,2))
if mibBuilder.loadTexts:automationSimaticNetAgentCapability.setStatus(_A)
_AutomationMotionControlAgentCapability_ObjectIdentity=ObjectIdentity
automationMotionControlAgentCapability=_AutomationMotionControlAgentCapability_ObjectIdentity((1,3,6,1,4,1,4329,6,4,3))
if mibBuilder.loadTexts:automationMotionControlAgentCapability.setStatus(_A)
_AutomationHmiAgentCapability_ObjectIdentity=ObjectIdentity
automationHmiAgentCapability=_AutomationHmiAgentCapability_ObjectIdentity((1,3,6,1,4,1,4329,6,4,4))
if mibBuilder.loadTexts:automationHmiAgentCapability.setStatus(_A)
_AutomationSitopPowerCapability_ObjectIdentity=ObjectIdentity
automationSitopPowerCapability=_AutomationSitopPowerCapability_ObjectIdentity((1,3,6,1,4,1,4329,6,4,5))
if mibBuilder.loadTexts:automationSitopPowerCapability.setStatus(_A)
mibBuilder.exportSymbols('AUTOMATION-SMI',**{'automation':automation,'automationProducts':automationProducts,'automationPlc':automationPlc,'automationSimaticNet':automationSimaticNet,'automationMotionControl':automationMotionControl,'automationHmi':automationHmi,'automationSitopPower':automationSitopPower,'automationModules':automationModules,'automationMgmt':automationMgmt,'automationAgentCapability':automationAgentCapability,'automationPlcAgentCapability':automationPlcAgentCapability,'automationSimaticNetAgentCapability':automationSimaticNetAgentCapability,'automationMotionControlAgentCapability':automationMotionControlAgentCapability,'automationHmiAgentCapability':automationHmiAgentCapability,'automationSitopPowerCapability':automationSitopPowerCapability})