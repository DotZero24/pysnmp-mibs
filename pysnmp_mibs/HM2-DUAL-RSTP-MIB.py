_L='hm2DualRstpMstId'
_K='HM2-DUAL-RSTP-MIB'
_J='ifIndex'
_I='IF-MIB'
_H='Integer32'
_G='InterfaceIndexOrZero'
_F='OctetString'
_E='HmEnabledStatus'
_D='Unsigned32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HmEnabledStatus,hm2ConfigurationMibs=mibBuilder.importSymbols('HM2-TC-MIB',_E,'hm2ConfigurationMibs')
InterfaceIndex,InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_I,'InterfaceIndex',_G,_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
hm2DualRstpMib=ModuleIdentity((1,3,6,1,4,1,248,11,150))
if mibBuilder.loadTexts:hm2DualRstpMib.setRevisions(('2019-03-29 00:00',))
_Hm2DualRstpMibNotifications_ObjectIdentity=ObjectIdentity
hm2DualRstpMibNotifications=_Hm2DualRstpMibNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,150,0))
_Hm2DualRstpMibObjects_ObjectIdentity=ObjectIdentity
hm2DualRstpMibObjects=_Hm2DualRstpMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,150,1))
_Hm2DualRstpCstConfigGroup_ObjectIdentity=ObjectIdentity
hm2DualRstpCstConfigGroup=_Hm2DualRstpCstConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,11,150,1,0))
class _Hm2DualRstpAdminMode_Type(HmEnabledStatus):defaultValue=2
_Hm2DualRstpAdminMode_Type.__name__=_E
_Hm2DualRstpAdminMode_Object=MibScalar
hm2DualRstpAdminMode=_Hm2DualRstpAdminMode_Object((1,3,6,1,4,1,248,11,150,1,0,1),_Hm2DualRstpAdminMode_Type())
hm2DualRstpAdminMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DualRstpAdminMode.setStatus(_A)
_Hm2DualRstpCstHelloTime_Type=Unsigned32
_Hm2DualRstpCstHelloTime_Object=MibScalar
hm2DualRstpCstHelloTime=_Hm2DualRstpCstHelloTime_Object((1,3,6,1,4,1,248,11,150,1,0,2),_Hm2DualRstpCstHelloTime_Type())
hm2DualRstpCstHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DualRstpCstHelloTime.setStatus(_A)
_Hm2DualRstpCstMaxAge_Type=Unsigned32
_Hm2DualRstpCstMaxAge_Object=MibScalar
hm2DualRstpCstMaxAge=_Hm2DualRstpCstMaxAge_Object((1,3,6,1,4,1,248,11,150,1,0,3),_Hm2DualRstpCstMaxAge_Type())
hm2DualRstpCstMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DualRstpCstMaxAge.setStatus(_A)
class _Hm2DualRstpCstRegionalRootId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_Hm2DualRstpCstRegionalRootId_Type.__name__=_F
_Hm2DualRstpCstRegionalRootId_Object=MibScalar
hm2DualRstpCstRegionalRootId=_Hm2DualRstpCstRegionalRootId_Object((1,3,6,1,4,1,248,11,150,1,0,4),_Hm2DualRstpCstRegionalRootId_Type())
hm2DualRstpCstRegionalRootId.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DualRstpCstRegionalRootId.setStatus(_A)
_Hm2DualRstpCstRegionalRootPathCost_Type=Unsigned32
_Hm2DualRstpCstRegionalRootPathCost_Object=MibScalar
hm2DualRstpCstRegionalRootPathCost=_Hm2DualRstpCstRegionalRootPathCost_Object((1,3,6,1,4,1,248,11,150,1,0,5),_Hm2DualRstpCstRegionalRootPathCost_Type())
hm2DualRstpCstRegionalRootPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DualRstpCstRegionalRootPathCost.setStatus(_A)
_Hm2DualRstpCstRootFwdDelay_Type=Unsigned32
_Hm2DualRstpCstRootFwdDelay_Object=MibScalar
hm2DualRstpCstRootFwdDelay=_Hm2DualRstpCstRootFwdDelay_Object((1,3,6,1,4,1,248,11,150,1,0,6),_Hm2DualRstpCstRootFwdDelay_Type())
hm2DualRstpCstRootFwdDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DualRstpCstRootFwdDelay.setStatus(_A)
class _Hm2DualRstpCstBridgeMaxAge_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_Hm2DualRstpCstBridgeMaxAge_Type.__name__=_D
_Hm2DualRstpCstBridgeMaxAge_Object=MibScalar
hm2DualRstpCstBridgeMaxAge=_Hm2DualRstpCstBridgeMaxAge_Object((1,3,6,1,4,1,248,11,150,1,0,7),_Hm2DualRstpCstBridgeMaxAge_Type())
hm2DualRstpCstBridgeMaxAge.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DualRstpCstBridgeMaxAge.setStatus(_A)
class _Hm2DualRstpCstBridgeHelloTime_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Hm2DualRstpCstBridgeHelloTime_Type.__name__=_D
_Hm2DualRstpCstBridgeHelloTime_Object=MibScalar
hm2DualRstpCstBridgeHelloTime=_Hm2DualRstpCstBridgeHelloTime_Object((1,3,6,1,4,1,248,11,150,1,0,8),_Hm2DualRstpCstBridgeHelloTime_Type())
hm2DualRstpCstBridgeHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DualRstpCstBridgeHelloTime.setStatus(_A)
_Hm2DualRstpCstBridgeHoldTime_Type=Unsigned32
_Hm2DualRstpCstBridgeHoldTime_Object=MibScalar
hm2DualRstpCstBridgeHoldTime=_Hm2DualRstpCstBridgeHoldTime_Object((1,3,6,1,4,1,248,11,150,1,0,9),_Hm2DualRstpCstBridgeHoldTime_Type())
hm2DualRstpCstBridgeHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DualRstpCstBridgeHoldTime.setStatus(_A)
class _Hm2DualRstpCstBridgeFwdDelay_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_Hm2DualRstpCstBridgeFwdDelay_Type.__name__=_D
_Hm2DualRstpCstBridgeFwdDelay_Object=MibScalar
hm2DualRstpCstBridgeFwdDelay=_Hm2DualRstpCstBridgeFwdDelay_Object((1,3,6,1,4,1,248,11,150,1,0,10),_Hm2DualRstpCstBridgeFwdDelay_Type())
hm2DualRstpCstBridgeFwdDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DualRstpCstBridgeFwdDelay.setStatus(_A)
class _Hm2DualRstpCstBridgeMaxHops_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_Hm2DualRstpCstBridgeMaxHops_Type.__name__=_D
_Hm2DualRstpCstBridgeMaxHops_Object=MibScalar
hm2DualRstpCstBridgeMaxHops=_Hm2DualRstpCstBridgeMaxHops_Object((1,3,6,1,4,1,248,11,150,1,0,11),_Hm2DualRstpCstBridgeMaxHops_Type())
hm2DualRstpCstBridgeMaxHops.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DualRstpCstBridgeMaxHops.setStatus(_A)
class _Hm2DualRstpCstBridgePriority_Type(Unsigned32):defaultValue=32768;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_Hm2DualRstpCstBridgePriority_Type.__name__=_D
_Hm2DualRstpCstBridgePriority_Object=MibScalar
hm2DualRstpCstBridgePriority=_Hm2DualRstpCstBridgePriority_Object((1,3,6,1,4,1,248,11,150,1,0,12),_Hm2DualRstpCstBridgePriority_Type())
hm2DualRstpCstBridgePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DualRstpCstBridgePriority.setStatus(_A)
_Hm2DualRstpCstBridgeTimeSinceTopologyChange_Type=TimeTicks
_Hm2DualRstpCstBridgeTimeSinceTopologyChange_Object=MibScalar
hm2DualRstpCstBridgeTimeSinceTopologyChange=_Hm2DualRstpCstBridgeTimeSinceTopologyChange_Object((1,3,6,1,4,1,248,11,150,1,0,13),_Hm2DualRstpCstBridgeTimeSinceTopologyChange_Type())
hm2DualRstpCstBridgeTimeSinceTopologyChange.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DualRstpCstBridgeTimeSinceTopologyChange.setStatus(_A)
_Hm2DualRstpCstBridgeTopChanges_Type=Counter32
_Hm2DualRstpCstBridgeTopChanges_Object=MibScalar
hm2DualRstpCstBridgeTopChanges=_Hm2DualRstpCstBridgeTopChanges_Object((1,3,6,1,4,1,248,11,150,1,0,14),_Hm2DualRstpCstBridgeTopChanges_Type())
hm2DualRstpCstBridgeTopChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DualRstpCstBridgeTopChanges.setStatus(_A)
class _Hm2DualRstpCstBridgeTopologyChangeParm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_Hm2DualRstpCstBridgeTopologyChangeParm_Type.__name__=_H
_Hm2DualRstpCstBridgeTopologyChangeParm_Object=MibScalar
hm2DualRstpCstBridgeTopologyChangeParm=_Hm2DualRstpCstBridgeTopologyChangeParm_Object((1,3,6,1,4,1,248,11,150,1,0,15),_Hm2DualRstpCstBridgeTopologyChangeParm_Type())
hm2DualRstpCstBridgeTopologyChangeParm.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DualRstpCstBridgeTopologyChangeParm.setStatus(_A)
_Hm2DualRstpCstBridgeRootCost_Type=Unsigned32
_Hm2DualRstpCstBridgeRootCost_Object=MibScalar
hm2DualRstpCstBridgeRootCost=_Hm2DualRstpCstBridgeRootCost_Object((1,3,6,1,4,1,248,11,150,1,0,16),_Hm2DualRstpCstBridgeRootCost_Type())
hm2DualRstpCstBridgeRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DualRstpCstBridgeRootCost.setStatus(_A)
class _Hm2DualRstpCstBridgeRootPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_Hm2DualRstpCstBridgeRootPort_Type.__name__=_F
_Hm2DualRstpCstBridgeRootPort_Object=MibScalar
hm2DualRstpCstBridgeRootPort=_Hm2DualRstpCstBridgeRootPort_Object((1,3,6,1,4,1,248,11,150,1,0,17),_Hm2DualRstpCstBridgeRootPort_Type())
hm2DualRstpCstBridgeRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DualRstpCstBridgeRootPort.setStatus(_A)
class _Hm2DualRstpCstBridgeHoldCount_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,40))
_Hm2DualRstpCstBridgeHoldCount_Type.__name__=_D
_Hm2DualRstpCstBridgeHoldCount_Object=MibScalar
hm2DualRstpCstBridgeHoldCount=_Hm2DualRstpCstBridgeHoldCount_Object((1,3,6,1,4,1,248,11,150,1,0,18),_Hm2DualRstpCstBridgeHoldCount_Type())
hm2DualRstpCstBridgeHoldCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DualRstpCstBridgeHoldCount.setStatus(_A)
class _Hm2DualRstpBpduGuardMode_Type(HmEnabledStatus):defaultValue=2
_Hm2DualRstpBpduGuardMode_Type.__name__=_E
_Hm2DualRstpBpduGuardMode_Object=MibScalar
hm2DualRstpBpduGuardMode=_Hm2DualRstpBpduGuardMode_Object((1,3,6,1,4,1,248,11,150,1,0,19),_Hm2DualRstpBpduGuardMode_Type())
hm2DualRstpBpduGuardMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DualRstpBpduGuardMode.setStatus(_A)
class _Hm2DualRstpBpduFilterDefault_Type(HmEnabledStatus):defaultValue=2
_Hm2DualRstpBpduFilterDefault_Type.__name__=_E
_Hm2DualRstpBpduFilterDefault_Object=MibScalar
hm2DualRstpBpduFilterDefault=_Hm2DualRstpBpduFilterDefault_Object((1,3,6,1,4,1,248,11,150,1,0,20),_Hm2DualRstpBpduFilterDefault_Type())
hm2DualRstpBpduFilterDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DualRstpBpduFilterDefault.setStatus(_A)
class _Hm2DualRstpBridgeIdentifier_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_Hm2DualRstpBridgeIdentifier_Type.__name__=_F
_Hm2DualRstpBridgeIdentifier_Object=MibScalar
hm2DualRstpBridgeIdentifier=_Hm2DualRstpBridgeIdentifier_Object((1,3,6,1,4,1,248,11,150,1,0,21),_Hm2DualRstpBridgeIdentifier_Type())
hm2DualRstpBridgeIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DualRstpBridgeIdentifier.setStatus(_A)
class _Hm2DualRstpCstBridgeDesignatedRoot_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_Hm2DualRstpCstBridgeDesignatedRoot_Type.__name__=_F
_Hm2DualRstpCstBridgeDesignatedRoot_Object=MibScalar
hm2DualRstpCstBridgeDesignatedRoot=_Hm2DualRstpCstBridgeDesignatedRoot_Object((1,3,6,1,4,1,248,11,150,1,0,22),_Hm2DualRstpCstBridgeDesignatedRoot_Type())
hm2DualRstpCstBridgeDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DualRstpCstBridgeDesignatedRoot.setStatus(_A)
class _Hm2DualRstpRingOnlyMode_Type(HmEnabledStatus):defaultValue=2
_Hm2DualRstpRingOnlyMode_Type.__name__=_E
_Hm2DualRstpRingOnlyMode_Object=MibScalar
hm2DualRstpRingOnlyMode=_Hm2DualRstpRingOnlyMode_Object((1,3,6,1,4,1,248,11,150,1,0,23),_Hm2DualRstpRingOnlyMode_Type())
hm2DualRstpRingOnlyMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DualRstpRingOnlyMode.setStatus(_A)
class _Hm2DualRstpRingOnlyModeIntfOne_Type(InterfaceIndexOrZero):defaultValue=0
_Hm2DualRstpRingOnlyModeIntfOne_Type.__name__=_G
_Hm2DualRstpRingOnlyModeIntfOne_Object=MibScalar
hm2DualRstpRingOnlyModeIntfOne=_Hm2DualRstpRingOnlyModeIntfOne_Object((1,3,6,1,4,1,248,11,150,1,0,24),_Hm2DualRstpRingOnlyModeIntfOne_Type())
hm2DualRstpRingOnlyModeIntfOne.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DualRstpRingOnlyModeIntfOne.setStatus(_A)
class _Hm2DualRstpRingOnlyModeIntfTwo_Type(InterfaceIndexOrZero):defaultValue=0
_Hm2DualRstpRingOnlyModeIntfTwo_Type.__name__=_G
_Hm2DualRstpRingOnlyModeIntfTwo_Object=MibScalar
hm2DualRstpRingOnlyModeIntfTwo=_Hm2DualRstpRingOnlyModeIntfTwo_Object((1,3,6,1,4,1,248,11,150,1,0,25),_Hm2DualRstpRingOnlyModeIntfTwo_Type())
hm2DualRstpRingOnlyModeIntfTwo.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DualRstpRingOnlyModeIntfTwo.setStatus(_A)
class _Hm2DualRstpTrapMode_Type(HmEnabledStatus):defaultValue=1
_Hm2DualRstpTrapMode_Type.__name__=_E
_Hm2DualRstpTrapMode_Object=MibScalar
hm2DualRstpTrapMode=_Hm2DualRstpTrapMode_Object((1,3,6,1,4,1,248,11,150,1,0,26),_Hm2DualRstpTrapMode_Type())
hm2DualRstpTrapMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DualRstpTrapMode.setStatus(_A)
class _Hm2DualRstpMstId_Type(Unsigned32):defaultValue=0
_Hm2DualRstpMstId_Type.__name__=_D
_Hm2DualRstpMstId_Object=MibScalar
hm2DualRstpMstId=_Hm2DualRstpMstId_Object((1,3,6,1,4,1,248,11,150,1,0,27),_Hm2DualRstpMstId_Type())
hm2DualRstpMstId.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DualRstpMstId.setStatus(_A)
_Hm2DualRstpCstPortConfigGroup_ObjectIdentity=ObjectIdentity
hm2DualRstpCstPortConfigGroup=_Hm2DualRstpCstPortConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,11,150,1,1))
_Hm2DualRstpCstPortTable_Object=MibTable
hm2DualRstpCstPortTable=_Hm2DualRstpCstPortTable_Object((1,3,6,1,4,1,248,11,150,1,1,1))
if mibBuilder.loadTexts:hm2DualRstpCstPortTable.setStatus(_A)
_Hm2DualRstpCstPortEntry_Object=MibTableRow
hm2DualRstpCstPortEntry=_Hm2DualRstpCstPortEntry_Object((1,3,6,1,4,1,248,11,150,1,1,1,1))
hm2DualRstpCstPortEntry.setIndexNames((0,_K,_L),(0,_I,_J))
if mibBuilder.loadTexts:hm2DualRstpCstPortEntry.setStatus(_A)
class _Hm2DualRstpCstPortDrstpInstance_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_Hm2DualRstpCstPortDrstpInstance_Type.__name__=_H
_Hm2DualRstpCstPortDrstpInstance_Object=MibTableColumn
hm2DualRstpCstPortDrstpInstance=_Hm2DualRstpCstPortDrstpInstance_Object((1,3,6,1,4,1,248,11,150,1,1,1,1,1),_Hm2DualRstpCstPortDrstpInstance_Type())
hm2DualRstpCstPortDrstpInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DualRstpCstPortDrstpInstance.setStatus(_A)
mibBuilder.exportSymbols(_K,**{'hm2DualRstpMib':hm2DualRstpMib,'hm2DualRstpMibNotifications':hm2DualRstpMibNotifications,'hm2DualRstpMibObjects':hm2DualRstpMibObjects,'hm2DualRstpCstConfigGroup':hm2DualRstpCstConfigGroup,'hm2DualRstpAdminMode':hm2DualRstpAdminMode,'hm2DualRstpCstHelloTime':hm2DualRstpCstHelloTime,'hm2DualRstpCstMaxAge':hm2DualRstpCstMaxAge,'hm2DualRstpCstRegionalRootId':hm2DualRstpCstRegionalRootId,'hm2DualRstpCstRegionalRootPathCost':hm2DualRstpCstRegionalRootPathCost,'hm2DualRstpCstRootFwdDelay':hm2DualRstpCstRootFwdDelay,'hm2DualRstpCstBridgeMaxAge':hm2DualRstpCstBridgeMaxAge,'hm2DualRstpCstBridgeHelloTime':hm2DualRstpCstBridgeHelloTime,'hm2DualRstpCstBridgeHoldTime':hm2DualRstpCstBridgeHoldTime,'hm2DualRstpCstBridgeFwdDelay':hm2DualRstpCstBridgeFwdDelay,'hm2DualRstpCstBridgeMaxHops':hm2DualRstpCstBridgeMaxHops,'hm2DualRstpCstBridgePriority':hm2DualRstpCstBridgePriority,'hm2DualRstpCstBridgeTimeSinceTopologyChange':hm2DualRstpCstBridgeTimeSinceTopologyChange,'hm2DualRstpCstBridgeTopChanges':hm2DualRstpCstBridgeTopChanges,'hm2DualRstpCstBridgeTopologyChangeParm':hm2DualRstpCstBridgeTopologyChangeParm,'hm2DualRstpCstBridgeRootCost':hm2DualRstpCstBridgeRootCost,'hm2DualRstpCstBridgeRootPort':hm2DualRstpCstBridgeRootPort,'hm2DualRstpCstBridgeHoldCount':hm2DualRstpCstBridgeHoldCount,'hm2DualRstpBpduGuardMode':hm2DualRstpBpduGuardMode,'hm2DualRstpBpduFilterDefault':hm2DualRstpBpduFilterDefault,'hm2DualRstpBridgeIdentifier':hm2DualRstpBridgeIdentifier,'hm2DualRstpCstBridgeDesignatedRoot':hm2DualRstpCstBridgeDesignatedRoot,'hm2DualRstpRingOnlyMode':hm2DualRstpRingOnlyMode,'hm2DualRstpRingOnlyModeIntfOne':hm2DualRstpRingOnlyModeIntfOne,'hm2DualRstpRingOnlyModeIntfTwo':hm2DualRstpRingOnlyModeIntfTwo,'hm2DualRstpTrapMode':hm2DualRstpTrapMode,_L:hm2DualRstpMstId,'hm2DualRstpCstPortConfigGroup':hm2DualRstpCstPortConfigGroup,'hm2DualRstpCstPortTable':hm2DualRstpCstPortTable,'hm2DualRstpCstPortEntry':hm2DualRstpCstPortEntry,'hm2DualRstpCstPortDrstpInstance':hm2DualRstpCstPortDrstpInstance})