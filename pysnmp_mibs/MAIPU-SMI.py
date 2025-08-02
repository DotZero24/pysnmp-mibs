_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
maipu=ModuleIdentity((1,3,6,1,4,1,5651))
if mibBuilder.loadTexts:maipu.setRevisions(('1901-01-01 00:00',))
_MpProducts_ObjectIdentity=ObjectIdentity
mpProducts=_MpProducts_ObjectIdentity((1,3,6,1,4,1,5651,1))
if mibBuilder.loadTexts:mpProducts.setStatus(_A)
_MpTrapObject_ObjectIdentity=ObjectIdentity
mpTrapObject=_MpTrapObject_ObjectIdentity((1,3,6,1,4,1,5651,2))
if mibBuilder.loadTexts:mpTrapObject.setStatus(_A)
_MpMgmt_ObjectIdentity=ObjectIdentity
mpMgmt=_MpMgmt_ObjectIdentity((1,3,6,1,4,1,5651,3))
if mibBuilder.loadTexts:mpMgmt.setStatus(_A)
_MpExperiment_ObjectIdentity=ObjectIdentity
mpExperiment=_MpExperiment_ObjectIdentity((1,3,6,1,4,1,5651,4))
if mibBuilder.loadTexts:mpExperiment.setStatus(_A)
_MpSecurity_ObjectIdentity=ObjectIdentity
mpSecurity=_MpSecurity_ObjectIdentity((1,3,6,1,4,1,5651,5))
if mibBuilder.loadTexts:mpSecurity.setStatus(_A)
_MpMgmt2_ObjectIdentity=ObjectIdentity
mpMgmt2=_MpMgmt2_ObjectIdentity((1,3,6,1,4,1,5651,6))
if mibBuilder.loadTexts:mpMgmt2.setStatus(_A)
_MpSystem_ObjectIdentity=ObjectIdentity
mpSystem=_MpSystem_ObjectIdentity((1,3,6,1,4,1,5651,6,1))
if mibBuilder.loadTexts:mpSystem.setStatus(_A)
_MpRouterTech_ObjectIdentity=ObjectIdentity
mpRouterTech=_MpRouterTech_ObjectIdentity((1,3,6,1,4,1,5651,6,2))
if mibBuilder.loadTexts:mpRouterTech.setStatus(_A)
_MpSwitchTech_ObjectIdentity=ObjectIdentity
mpSwitchTech=_MpSwitchTech_ObjectIdentity((1,3,6,1,4,1,5651,6,3))
if mibBuilder.loadTexts:mpSwitchTech.setStatus(_A)
_MpVoipTech_ObjectIdentity=ObjectIdentity
mpVoipTech=_MpVoipTech_ObjectIdentity((1,3,6,1,4,1,5651,6,4))
if mibBuilder.loadTexts:mpVoipTech.setStatus(_A)
_MpSecurityTech_ObjectIdentity=ObjectIdentity
mpSecurityTech=_MpSecurityTech_ObjectIdentity((1,3,6,1,4,1,5651,6,5))
if mibBuilder.loadTexts:mpSecurityTech.setStatus(_A)
_MpApp_ObjectIdentity=ObjectIdentity
mpApp=_MpApp_ObjectIdentity((1,3,6,1,4,1,5651,6,6))
if mibBuilder.loadTexts:mpApp.setStatus(_A)
_MpOtherSys_ObjectIdentity=ObjectIdentity
mpOtherSys=_MpOtherSys_ObjectIdentity((1,3,6,1,4,1,5651,6,7))
if mibBuilder.loadTexts:mpOtherSys.setStatus(_A)
mibBuilder.exportSymbols('MAIPU-SMI',**{'maipu':maipu,'mpProducts':mpProducts,'mpTrapObject':mpTrapObject,'mpMgmt':mpMgmt,'mpExperiment':mpExperiment,'mpSecurity':mpSecurity,'mpMgmt2':mpMgmt2,'mpSystem':mpSystem,'mpRouterTech':mpRouterTech,'mpSwitchTech':mpSwitchTech,'mpVoipTech':mpVoipTech,'mpSecurityTech':mpSecurityTech,'mpApp':mpApp,'mpOtherSys':mpOtherSys})