_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hirschmann=ModuleIdentity((1,3,6,1,4,1,248))
if mibBuilder.loadTexts:hirschmann.setRevisions(('2010-01-08 17:00',))
_HmVendor_ObjectIdentity=ObjectIdentity
hmVendor=_HmVendor_ObjectIdentity((1,3,6,1,4,1,248,100))
if mibBuilder.loadTexts:hmVendor.setStatus(_A)
_HmITSwitch_ObjectIdentity=ObjectIdentity
hmITSwitch=_HmITSwitch_ObjectIdentity((1,3,6,1,4,1,248,100,1))
if mibBuilder.loadTexts:hmITSwitch.setStatus(_A)
_HmITProducts_ObjectIdentity=ObjectIdentity
hmITProducts=_HmITProducts_ObjectIdentity((1,3,6,1,4,1,248,100,1,1))
if mibBuilder.loadTexts:hmITProducts.setStatus(_A)
_HmITTrapObject_ObjectIdentity=ObjectIdentity
hmITTrapObject=_HmITTrapObject_ObjectIdentity((1,3,6,1,4,1,248,100,1,2))
if mibBuilder.loadTexts:hmITTrapObject.setStatus(_A)
_HmITMgmt_ObjectIdentity=ObjectIdentity
hmITMgmt=_HmITMgmt_ObjectIdentity((1,3,6,1,4,1,248,100,1,3))
if mibBuilder.loadTexts:hmITMgmt.setStatus(_A)
_HmITExperiment_ObjectIdentity=ObjectIdentity
hmITExperiment=_HmITExperiment_ObjectIdentity((1,3,6,1,4,1,248,100,1,4))
if mibBuilder.loadTexts:hmITExperiment.setStatus(_A)
_HmITSecurity_ObjectIdentity=ObjectIdentity
hmITSecurity=_HmITSecurity_ObjectIdentity((1,3,6,1,4,1,248,100,1,5))
if mibBuilder.loadTexts:hmITSecurity.setStatus(_A)
_HmITMgmt2_ObjectIdentity=ObjectIdentity
hmITMgmt2=_HmITMgmt2_ObjectIdentity((1,3,6,1,4,1,248,100,1,6))
if mibBuilder.loadTexts:hmITMgmt2.setStatus(_A)
_HmITSystem_ObjectIdentity=ObjectIdentity
hmITSystem=_HmITSystem_ObjectIdentity((1,3,6,1,4,1,248,100,1,6,1))
if mibBuilder.loadTexts:hmITSystem.setStatus(_A)
_HmITRouterTech_ObjectIdentity=ObjectIdentity
hmITRouterTech=_HmITRouterTech_ObjectIdentity((1,3,6,1,4,1,248,100,1,6,2))
if mibBuilder.loadTexts:hmITRouterTech.setStatus(_A)
_HmITSwitchTech_ObjectIdentity=ObjectIdentity
hmITSwitchTech=_HmITSwitchTech_ObjectIdentity((1,3,6,1,4,1,248,100,1,6,3))
if mibBuilder.loadTexts:hmITSwitchTech.setStatus(_A)
_HmITVoipTech_ObjectIdentity=ObjectIdentity
hmITVoipTech=_HmITVoipTech_ObjectIdentity((1,3,6,1,4,1,248,100,1,6,4))
if mibBuilder.loadTexts:hmITVoipTech.setStatus(_A)
_HmITSecurityTech_ObjectIdentity=ObjectIdentity
hmITSecurityTech=_HmITSecurityTech_ObjectIdentity((1,3,6,1,4,1,248,100,1,6,5))
if mibBuilder.loadTexts:hmITSecurityTech.setStatus(_A)
_HmITApp_ObjectIdentity=ObjectIdentity
hmITApp=_HmITApp_ObjectIdentity((1,3,6,1,4,1,248,100,1,6,6))
if mibBuilder.loadTexts:hmITApp.setStatus(_A)
_HmITOtherSys_ObjectIdentity=ObjectIdentity
hmITOtherSys=_HmITOtherSys_ObjectIdentity((1,3,6,1,4,1,248,100,1,6,7))
if mibBuilder.loadTexts:hmITOtherSys.setStatus(_A)
mibBuilder.exportSymbols('HMIT-SMI',**{'hirschmann':hirschmann,'hmVendor':hmVendor,'hmITSwitch':hmITSwitch,'hmITProducts':hmITProducts,'hmITTrapObject':hmITTrapObject,'hmITMgmt':hmITMgmt,'hmITExperiment':hmITExperiment,'hmITSecurity':hmITSecurity,'hmITMgmt2':hmITMgmt2,'hmITSystem':hmITSystem,'hmITRouterTech':hmITRouterTech,'hmITSwitchTech':hmITSwitchTech,'hmITVoipTech':hmITVoipTech,'hmITSecurityTech':hmITSecurityTech,'hmITApp':hmITApp,'hmITOtherSys':hmITOtherSys})