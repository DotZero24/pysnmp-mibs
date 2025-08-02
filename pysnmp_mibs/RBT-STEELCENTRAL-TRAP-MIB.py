_P='alertMessage'
_O='alertInfoURL'
_N='alertURL'
_M='alertStart'
_L='alertID'
_K='alertPolicyEvalPeriod'
_J='alertPolicyType'
_I='alertPolicyID'
_H='alertPolicyDescription'
_G='alertPolicyName'
_F='alertSeverityLevel'
_E='alertSeverity'
_D='Integer32'
_C='accessible-for-notify'
_B='current'
_A='RBT-STEELCENTRAL-TRAP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
products,rbtTrap,rbtTrapInfo=mibBuilder.importSymbols('RBT-MIB','products','rbtTrap','rbtTrapInfo')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
steelcentralTrapModule=ModuleIdentity((1,3,6,1,4,1,17163,2,1))
if mibBuilder.loadTexts:steelcentralTrapModule.setRevisions(('2016-04-30 00:00',))
_SteelcentralTraps_ObjectIdentity=ObjectIdentity
steelcentralTraps=_SteelcentralTraps_ObjectIdentity((1,3,6,1,4,1,17163,2,1,1))
_SteelcentralTrapInfo_ObjectIdentity=ObjectIdentity
steelcentralTrapInfo=_SteelcentralTrapInfo_ObjectIdentity((1,3,6,1,4,1,17163,2,1,2))
class _AlertSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AlertSeverity_Type.__name__=_D
_AlertSeverity_Object=MibScalar
alertSeverity=_AlertSeverity_Object((1,3,6,1,4,1,17163,2,1,2,1),_AlertSeverity_Type())
alertSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:alertSeverity.setStatus(_B)
class _AlertSeverityLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('minor',1),('major',2),('critical',3)))
_AlertSeverityLevel_Type.__name__=_D
_AlertSeverityLevel_Object=MibScalar
alertSeverityLevel=_AlertSeverityLevel_Object((1,3,6,1,4,1,17163,2,1,2,2),_AlertSeverityLevel_Type())
alertSeverityLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:alertSeverityLevel.setStatus(_B)
_AlertPolicyName_Type=OctetString
_AlertPolicyName_Object=MibScalar
alertPolicyName=_AlertPolicyName_Object((1,3,6,1,4,1,17163,2,1,2,3),_AlertPolicyName_Type())
alertPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:alertPolicyName.setStatus(_B)
_AlertPolicyDescription_Type=OctetString
_AlertPolicyDescription_Object=MibScalar
alertPolicyDescription=_AlertPolicyDescription_Object((1,3,6,1,4,1,17163,2,1,2,4),_AlertPolicyDescription_Type())
alertPolicyDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:alertPolicyDescription.setStatus(_B)
_AlertPolicyID_Type=Integer32
_AlertPolicyID_Object=MibScalar
alertPolicyID=_AlertPolicyID_Object((1,3,6,1,4,1,17163,2,1,2,5),_AlertPolicyID_Type())
alertPolicyID.setMaxAccess(_C)
if mibBuilder.loadTexts:alertPolicyID.setStatus(_B)
class _AlertPolicyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('traffic',1),('storage',2),('watch',3),('pcap',4),('autobaseline',5)))
_AlertPolicyType_Type.__name__=_D
_AlertPolicyType_Object=MibScalar
alertPolicyType=_AlertPolicyType_Object((1,3,6,1,4,1,17163,2,1,2,6),_AlertPolicyType_Type())
alertPolicyType.setMaxAccess(_C)
if mibBuilder.loadTexts:alertPolicyType.setStatus(_B)
_AlertPolicyEvalPeriod_Type=Integer32
_AlertPolicyEvalPeriod_Object=MibScalar
alertPolicyEvalPeriod=_AlertPolicyEvalPeriod_Object((1,3,6,1,4,1,17163,2,1,2,7),_AlertPolicyEvalPeriod_Type())
alertPolicyEvalPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:alertPolicyEvalPeriod.setStatus(_B)
_AlertID_Type=Integer32
_AlertID_Object=MibScalar
alertID=_AlertID_Object((1,3,6,1,4,1,17163,2,1,2,8),_AlertID_Type())
alertID.setMaxAccess(_C)
if mibBuilder.loadTexts:alertID.setStatus(_B)
_AlertStart_Type=OctetString
_AlertStart_Object=MibScalar
alertStart=_AlertStart_Object((1,3,6,1,4,1,17163,2,1,2,9),_AlertStart_Type())
alertStart.setMaxAccess(_C)
if mibBuilder.loadTexts:alertStart.setStatus(_B)
_AlertURL_Type=OctetString
_AlertURL_Object=MibScalar
alertURL=_AlertURL_Object((1,3,6,1,4,1,17163,2,1,2,10),_AlertURL_Type())
alertURL.setMaxAccess(_C)
if mibBuilder.loadTexts:alertURL.setStatus(_B)
_AlertInfoURL_Type=OctetString
_AlertInfoURL_Object=MibScalar
alertInfoURL=_AlertInfoURL_Object((1,3,6,1,4,1,17163,2,1,2,11),_AlertInfoURL_Type())
alertInfoURL.setMaxAccess(_C)
if mibBuilder.loadTexts:alertInfoURL.setStatus(_B)
_AlertMessage_Type=OctetString
_AlertMessage_Object=MibScalar
alertMessage=_AlertMessage_Object((1,3,6,1,4,1,17163,2,1,2,12),_AlertMessage_Type())
alertMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:alertMessage.setStatus(_B)
testTrap=NotificationType((1,3,6,1,4,1,17163,2,1,1,1))
if mibBuilder.loadTexts:testTrap.setStatus(_B)
policyTrap=NotificationType((1,3,6,1,4,1,17163,2,1,1,2))
policyTrap.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:policyTrap.setStatus(_B)
hardwareTrap=NotificationType((1,3,6,1,4,1,17163,2,1,1,3))
hardwareTrap.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:hardwareTrap.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'steelcentralTrapModule':steelcentralTrapModule,'steelcentralTraps':steelcentralTraps,'testTrap':testTrap,'policyTrap':policyTrap,'hardwareTrap':hardwareTrap,'steelcentralTrapInfo':steelcentralTrapInfo,_E:alertSeverity,_F:alertSeverityLevel,_G:alertPolicyName,_H:alertPolicyDescription,_I:alertPolicyID,_J:alertPolicyType,_K:alertPolicyEvalPeriod,_L:alertID,_M:alertStart,_N:alertURL,_O:alertInfoURL,_P:alertMessage})