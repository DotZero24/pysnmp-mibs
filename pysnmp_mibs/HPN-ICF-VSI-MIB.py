_P='hpnicfVsiIfID'
_O='hpnicfVsiLocalMacAddr'
_N='hpnicfVsiFloodMac'
_M='hpnicfVsiPwIndex'
_L='hpnicfVsiXconnectEvcSrvInstId'
_K='hpnicfVsiXconnectIfIndex'
_J='ethernet'
_I='OctetString'
_H='TruthValue'
_G='hpnicfVsiIndex'
_F='not-accessible'
_E='Integer32'
_D='HPN-ICF-VSI-MIB'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_H)
hpnicfVsi=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,105))
if mibBuilder.loadTexts:hpnicfVsi.setRevisions(('2009-08-08 10:00',))
_HpnicfVsiObjects_ObjectIdentity=ObjectIdentity
hpnicfVsiObjects=_HpnicfVsiObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,105,1))
_HpnicfVsiScalarGroup_ObjectIdentity=ObjectIdentity
hpnicfVsiScalarGroup=_HpnicfVsiScalarGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,105,1,1))
_HpnicfVsiNextAvailableVsiIndex_Type=Unsigned32
_HpnicfVsiNextAvailableVsiIndex_Object=MibScalar
hpnicfVsiNextAvailableVsiIndex=_HpnicfVsiNextAvailableVsiIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,1,1),_HpnicfVsiNextAvailableVsiIndex_Type())
hpnicfVsiNextAvailableVsiIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsiNextAvailableVsiIndex.setStatus(_A)
_HpnicfVsiL2vpnStatus_Type=TruthValue
_HpnicfVsiL2vpnStatus_Object=MibScalar
hpnicfVsiL2vpnStatus=_HpnicfVsiL2vpnStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,1,2),_HpnicfVsiL2vpnStatus_Type())
hpnicfVsiL2vpnStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpnicfVsiL2vpnStatus.setStatus(_A)
_HpnicfVsiTable_Object=MibTable
hpnicfVsiTable=_HpnicfVsiTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,2))
if mibBuilder.loadTexts:hpnicfVsiTable.setStatus(_A)
_HpnicfVsiEntry_Object=MibTableRow
hpnicfVsiEntry=_HpnicfVsiEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,2,1))
hpnicfVsiEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:hpnicfVsiEntry.setStatus(_A)
_HpnicfVsiIndex_Type=Unsigned32
_HpnicfVsiIndex_Object=MibTableColumn
hpnicfVsiIndex=_HpnicfVsiIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,2,1,1),_HpnicfVsiIndex_Type())
hpnicfVsiIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfVsiIndex.setStatus(_A)
class _HpnicfVsiName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HpnicfVsiName_Type.__name__=_I
_HpnicfVsiName_Object=MibTableColumn
hpnicfVsiName=_HpnicfVsiName_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,2,1,2),_HpnicfVsiName_Type())
hpnicfVsiName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVsiName.setStatus(_A)
class _HpnicfVsiMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('default',0),('martini',1),('minm',2),('martiniAndMinm',3),('kompella',4),('kompellaAndMinm',5),('minmpxp',6),('martiniAndMinmpxp',7),('kompellaAndMinmpxp',8)))
_HpnicfVsiMode_Type.__name__=_E
_HpnicfVsiMode_Object=MibTableColumn
hpnicfVsiMode=_HpnicfVsiMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,2,1,3),_HpnicfVsiMode_Type())
hpnicfVsiMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVsiMode.setStatus(_A)
_HpnicfMinmIsid_Type=Integer32
_HpnicfMinmIsid_Object=MibTableColumn
hpnicfMinmIsid=_HpnicfMinmIsid_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,2,1,4),_HpnicfMinmIsid_Type())
hpnicfMinmIsid.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMinmIsid.setStatus(_A)
_HpnicfVsiId_Type=Unsigned32
_HpnicfVsiId_Object=MibTableColumn
hpnicfVsiId=_HpnicfVsiId_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,2,1,5),_HpnicfVsiId_Type())
hpnicfVsiId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVsiId.setStatus(_A)
class _HpnicfVsiTransMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vlan',1),(_J,2)))
_HpnicfVsiTransMode_Type.__name__=_E
_HpnicfVsiTransMode_Object=MibTableColumn
hpnicfVsiTransMode=_HpnicfVsiTransMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,2,1,6),_HpnicfVsiTransMode_Type())
hpnicfVsiTransMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVsiTransMode.setStatus(_A)
class _HpnicfVsiEnableHubSpoke_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_HpnicfVsiEnableHubSpoke_Type.__name__=_E
_HpnicfVsiEnableHubSpoke_Object=MibTableColumn
hpnicfVsiEnableHubSpoke=_HpnicfVsiEnableHubSpoke_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,2,1,7),_HpnicfVsiEnableHubSpoke_Type())
hpnicfVsiEnableHubSpoke.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVsiEnableHubSpoke.setStatus(_A)
class _HpnicfVsiAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('adminUp',1),('adminDown',2)))
_HpnicfVsiAdminState_Type.__name__=_E
_HpnicfVsiAdminState_Object=MibTableColumn
hpnicfVsiAdminState=_HpnicfVsiAdminState_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,2,1,8),_HpnicfVsiAdminState_Type())
hpnicfVsiAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVsiAdminState.setStatus(_A)
_HpnicfVsiRowStatus_Type=RowStatus
_HpnicfVsiRowStatus_Object=MibTableColumn
hpnicfVsiRowStatus=_HpnicfVsiRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,2,1,9),_HpnicfVsiRowStatus_Type())
hpnicfVsiRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVsiRowStatus.setStatus(_A)
_HpnicfVsiSpbIsid_Type=Integer32
_HpnicfVsiSpbIsid_Object=MibTableColumn
hpnicfVsiSpbIsid=_HpnicfVsiSpbIsid_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,2,1,10),_HpnicfVsiSpbIsid_Type())
hpnicfVsiSpbIsid.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVsiSpbIsid.setStatus(_A)
_HpnicfVsiVxlanID_Type=Unsigned32
_HpnicfVsiVxlanID_Object=MibTableColumn
hpnicfVsiVxlanID=_HpnicfVsiVxlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,2,1,11),_HpnicfVsiVxlanID_Type())
hpnicfVsiVxlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsiVxlanID.setStatus(_A)
class _HpnicfVsiArpSuppression_Type(TruthValue):defaultValue=2
_HpnicfVsiArpSuppression_Type.__name__=_H
_HpnicfVsiArpSuppression_Object=MibTableColumn
hpnicfVsiArpSuppression=_HpnicfVsiArpSuppression_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,2,1,12),_HpnicfVsiArpSuppression_Type())
hpnicfVsiArpSuppression.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVsiArpSuppression.setStatus(_A)
class _HpnicfVsiFlooding_Type(TruthValue):defaultValue=1
_HpnicfVsiFlooding_Type.__name__=_H
_HpnicfVsiFlooding_Object=MibTableColumn
hpnicfVsiFlooding=_HpnicfVsiFlooding_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,2,1,13),_HpnicfVsiFlooding_Type())
hpnicfVsiFlooding.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVsiFlooding.setStatus(_A)
_HpnicfVsiLocalMacCount_Type=Unsigned32
_HpnicfVsiLocalMacCount_Object=MibTableColumn
hpnicfVsiLocalMacCount=_HpnicfVsiLocalMacCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,2,1,14),_HpnicfVsiLocalMacCount_Type())
hpnicfVsiLocalMacCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsiLocalMacCount.setStatus(_A)
_HpnicfVsiInterfaceID_Type=Unsigned32
_HpnicfVsiInterfaceID_Object=MibTableColumn
hpnicfVsiInterfaceID=_HpnicfVsiInterfaceID_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,2,1,15),_HpnicfVsiInterfaceID_Type())
hpnicfVsiInterfaceID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVsiInterfaceID.setStatus(_A)
class _HpnicfVsiStatistics_Type(TruthValue):defaultValue=2
_HpnicfVsiStatistics_Type.__name__=_H
_HpnicfVsiStatistics_Object=MibTableColumn
hpnicfVsiStatistics=_HpnicfVsiStatistics_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,2,1,16),_HpnicfVsiStatistics_Type())
hpnicfVsiStatistics.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVsiStatistics.setStatus(_A)
_HpnicfVsiNvgreID_Type=Unsigned32
_HpnicfVsiNvgreID_Object=MibTableColumn
hpnicfVsiNvgreID=_HpnicfVsiNvgreID_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,2,1,17),_HpnicfVsiNvgreID_Type())
hpnicfVsiNvgreID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsiNvgreID.setStatus(_A)
_HpnicfVsiXconnectTable_Object=MibTable
hpnicfVsiXconnectTable=_HpnicfVsiXconnectTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,3))
if mibBuilder.loadTexts:hpnicfVsiXconnectTable.setStatus(_A)
_HpnicfVsiXconnectEntry_Object=MibTableRow
hpnicfVsiXconnectEntry=_HpnicfVsiXconnectEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,3,1))
hpnicfVsiXconnectEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:hpnicfVsiXconnectEntry.setStatus(_A)
_HpnicfVsiXconnectIfIndex_Type=Unsigned32
_HpnicfVsiXconnectIfIndex_Object=MibTableColumn
hpnicfVsiXconnectIfIndex=_HpnicfVsiXconnectIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,3,1,1),_HpnicfVsiXconnectIfIndex_Type())
hpnicfVsiXconnectIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfVsiXconnectIfIndex.setStatus(_A)
_HpnicfVsiXconnectEvcSrvInstId_Type=Unsigned32
_HpnicfVsiXconnectEvcSrvInstId_Object=MibTableColumn
hpnicfVsiXconnectEvcSrvInstId=_HpnicfVsiXconnectEvcSrvInstId_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,3,1,2),_HpnicfVsiXconnectEvcSrvInstId_Type())
hpnicfVsiXconnectEvcSrvInstId.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfVsiXconnectEvcSrvInstId.setStatus(_A)
class _HpnicfVsiXconnectVsiName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HpnicfVsiXconnectVsiName_Type.__name__=_I
_HpnicfVsiXconnectVsiName_Object=MibTableColumn
hpnicfVsiXconnectVsiName=_HpnicfVsiXconnectVsiName_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,3,1,3),_HpnicfVsiXconnectVsiName_Type())
hpnicfVsiXconnectVsiName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVsiXconnectVsiName.setStatus(_A)
class _HpnicfVsiXconnectAccessMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vlan',1),(_J,2)))
_HpnicfVsiXconnectAccessMode_Type.__name__=_E
_HpnicfVsiXconnectAccessMode_Object=MibTableColumn
hpnicfVsiXconnectAccessMode=_HpnicfVsiXconnectAccessMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,3,1,4),_HpnicfVsiXconnectAccessMode_Type())
hpnicfVsiXconnectAccessMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVsiXconnectAccessMode.setStatus(_A)
class _HpnicfVsiXconnectHubSpoke_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('hub',2),('spoke',3)))
_HpnicfVsiXconnectHubSpoke_Type.__name__=_E
_HpnicfVsiXconnectHubSpoke_Object=MibTableColumn
hpnicfVsiXconnectHubSpoke=_HpnicfVsiXconnectHubSpoke_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,3,1,5),_HpnicfVsiXconnectHubSpoke_Type())
hpnicfVsiXconnectHubSpoke.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVsiXconnectHubSpoke.setStatus(_A)
_HpnicfVsiXconnectRowStatus_Type=RowStatus
_HpnicfVsiXconnectRowStatus_Object=MibTableColumn
hpnicfVsiXconnectRowStatus=_HpnicfVsiXconnectRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,3,1,6),_HpnicfVsiXconnectRowStatus_Type())
hpnicfVsiXconnectRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVsiXconnectRowStatus.setStatus(_A)
_HpnicfVsiPwBindTable_Object=MibTable
hpnicfVsiPwBindTable=_HpnicfVsiPwBindTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,4))
if mibBuilder.loadTexts:hpnicfVsiPwBindTable.setStatus(_A)
_HpnicfVsiPwBindEntry_Object=MibTableRow
hpnicfVsiPwBindEntry=_HpnicfVsiPwBindEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,4,1))
hpnicfVsiPwBindEntry.setIndexNames((0,_D,_G),(0,_D,_M))
if mibBuilder.loadTexts:hpnicfVsiPwBindEntry.setStatus(_A)
_HpnicfVsiPwIndex_Type=Unsigned32
_HpnicfVsiPwIndex_Object=MibTableColumn
hpnicfVsiPwIndex=_HpnicfVsiPwIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,4,1,1),_HpnicfVsiPwIndex_Type())
hpnicfVsiPwIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfVsiPwIndex.setStatus(_A)
class _HpnicfVsiPwBindAttributes_Type(Bits):namedValues=NamedValues(*(('noSplitHorizon',0),('hub',1)))
_HpnicfVsiPwBindAttributes_Type.__name__='Bits'
_HpnicfVsiPwBindAttributes_Object=MibTableColumn
hpnicfVsiPwBindAttributes=_HpnicfVsiPwBindAttributes_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,4,1,2),_HpnicfVsiPwBindAttributes_Type())
hpnicfVsiPwBindAttributes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVsiPwBindAttributes.setStatus(_A)
_HpnicfVsiPwBindRowStatus_Type=RowStatus
_HpnicfVsiPwBindRowStatus_Object=MibTableColumn
hpnicfVsiPwBindRowStatus=_HpnicfVsiPwBindRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,4,1,3),_HpnicfVsiPwBindRowStatus_Type())
hpnicfVsiPwBindRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVsiPwBindRowStatus.setStatus(_A)
_HpnicfVsiFloodMacTable_Object=MibTable
hpnicfVsiFloodMacTable=_HpnicfVsiFloodMacTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,5))
if mibBuilder.loadTexts:hpnicfVsiFloodMacTable.setStatus(_A)
_HpnicfVsiFloodMacEntry_Object=MibTableRow
hpnicfVsiFloodMacEntry=_HpnicfVsiFloodMacEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,5,1))
hpnicfVsiFloodMacEntry.setIndexNames((0,_D,_G),(0,_D,_N))
if mibBuilder.loadTexts:hpnicfVsiFloodMacEntry.setStatus(_A)
_HpnicfVsiFloodMac_Type=MacAddress
_HpnicfVsiFloodMac_Object=MibTableColumn
hpnicfVsiFloodMac=_HpnicfVsiFloodMac_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,5,1,1),_HpnicfVsiFloodMac_Type())
hpnicfVsiFloodMac.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfVsiFloodMac.setStatus(_A)
_HpnicfVsiFloodMacRowStatus_Type=RowStatus
_HpnicfVsiFloodMacRowStatus_Object=MibTableColumn
hpnicfVsiFloodMacRowStatus=_HpnicfVsiFloodMacRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,5,1,2),_HpnicfVsiFloodMacRowStatus_Type())
hpnicfVsiFloodMacRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVsiFloodMacRowStatus.setStatus(_A)
_HpnicfVsiLocalMacTable_Object=MibTable
hpnicfVsiLocalMacTable=_HpnicfVsiLocalMacTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,6))
if mibBuilder.loadTexts:hpnicfVsiLocalMacTable.setStatus(_A)
_HpnicfVsiLocalMacEntry_Object=MibTableRow
hpnicfVsiLocalMacEntry=_HpnicfVsiLocalMacEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,6,1))
hpnicfVsiLocalMacEntry.setIndexNames((0,_D,_G),(0,_D,_O))
if mibBuilder.loadTexts:hpnicfVsiLocalMacEntry.setStatus(_A)
_HpnicfVsiLocalMacAddr_Type=MacAddress
_HpnicfVsiLocalMacAddr_Object=MibTableColumn
hpnicfVsiLocalMacAddr=_HpnicfVsiLocalMacAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,6,1,1),_HpnicfVsiLocalMacAddr_Type())
hpnicfVsiLocalMacAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfVsiLocalMacAddr.setStatus(_A)
_HpnicfVsiLocalMacIfIndex_Type=InterfaceIndex
_HpnicfVsiLocalMacIfIndex_Object=MibTableColumn
hpnicfVsiLocalMacIfIndex=_HpnicfVsiLocalMacIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,6,1,2),_HpnicfVsiLocalMacIfIndex_Type())
hpnicfVsiLocalMacIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsiLocalMacIfIndex.setStatus(_A)
_HpnicfVsiLocalMacSrvID_Type=Unsigned32
_HpnicfVsiLocalMacSrvID_Object=MibTableColumn
hpnicfVsiLocalMacSrvID=_HpnicfVsiLocalMacSrvID_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,6,1,3),_HpnicfVsiLocalMacSrvID_Type())
hpnicfVsiLocalMacSrvID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsiLocalMacSrvID.setStatus(_A)
_HpnicfVsiPerfTable_Object=MibTable
hpnicfVsiPerfTable=_HpnicfVsiPerfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,7))
if mibBuilder.loadTexts:hpnicfVsiPerfTable.setStatus(_A)
_HpnicfVsiPerfEntry_Object=MibTableRow
hpnicfVsiPerfEntry=_HpnicfVsiPerfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,7,1))
hpnicfVsiPerfEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:hpnicfVsiPerfEntry.setStatus(_A)
_HpnicfVsiPerfInOctets_Type=Counter64
_HpnicfVsiPerfInOctets_Object=MibTableColumn
hpnicfVsiPerfInOctets=_HpnicfVsiPerfInOctets_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,7,1,1),_HpnicfVsiPerfInOctets_Type())
hpnicfVsiPerfInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsiPerfInOctets.setStatus(_A)
_HpnicfVsiPerfInPackets_Type=Counter64
_HpnicfVsiPerfInPackets_Object=MibTableColumn
hpnicfVsiPerfInPackets=_HpnicfVsiPerfInPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,7,1,2),_HpnicfVsiPerfInPackets_Type())
hpnicfVsiPerfInPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsiPerfInPackets.setStatus(_A)
_HpnicfVsiPerfInErrors_Type=Counter64
_HpnicfVsiPerfInErrors_Object=MibTableColumn
hpnicfVsiPerfInErrors=_HpnicfVsiPerfInErrors_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,7,1,3),_HpnicfVsiPerfInErrors_Type())
hpnicfVsiPerfInErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsiPerfInErrors.setStatus(_A)
_HpnicfVsiPerfInDiscards_Type=Counter64
_HpnicfVsiPerfInDiscards_Object=MibTableColumn
hpnicfVsiPerfInDiscards=_HpnicfVsiPerfInDiscards_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,7,1,4),_HpnicfVsiPerfInDiscards_Type())
hpnicfVsiPerfInDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsiPerfInDiscards.setStatus(_A)
_HpnicfVsiPerfOutOctets_Type=Counter64
_HpnicfVsiPerfOutOctets_Object=MibTableColumn
hpnicfVsiPerfOutOctets=_HpnicfVsiPerfOutOctets_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,7,1,5),_HpnicfVsiPerfOutOctets_Type())
hpnicfVsiPerfOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsiPerfOutOctets.setStatus(_A)
_HpnicfVsiPerfOutPackets_Type=Counter64
_HpnicfVsiPerfOutPackets_Object=MibTableColumn
hpnicfVsiPerfOutPackets=_HpnicfVsiPerfOutPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,7,1,6),_HpnicfVsiPerfOutPackets_Type())
hpnicfVsiPerfOutPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsiPerfOutPackets.setStatus(_A)
_HpnicfVsiPerfOutErrors_Type=Counter64
_HpnicfVsiPerfOutErrors_Object=MibTableColumn
hpnicfVsiPerfOutErrors=_HpnicfVsiPerfOutErrors_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,7,1,7),_HpnicfVsiPerfOutErrors_Type())
hpnicfVsiPerfOutErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsiPerfOutErrors.setStatus(_A)
_HpnicfVsiPerfOutDiscards_Type=Counter64
_HpnicfVsiPerfOutDiscards_Object=MibTableColumn
hpnicfVsiPerfOutDiscards=_HpnicfVsiPerfOutDiscards_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,7,1,8),_HpnicfVsiPerfOutDiscards_Type())
hpnicfVsiPerfOutDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsiPerfOutDiscards.setStatus(_A)
_HpnicfVsiNextAvailableVsiIfID_Type=Unsigned32
_HpnicfVsiNextAvailableVsiIfID_Object=MibScalar
hpnicfVsiNextAvailableVsiIfID=_HpnicfVsiNextAvailableVsiIfID_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,8),_HpnicfVsiNextAvailableVsiIfID_Type())
hpnicfVsiNextAvailableVsiIfID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsiNextAvailableVsiIfID.setStatus(_A)
_HpnicfVsiIfTable_Object=MibTable
hpnicfVsiIfTable=_HpnicfVsiIfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,9))
if mibBuilder.loadTexts:hpnicfVsiIfTable.setStatus(_A)
_HpnicfVsiIfEntry_Object=MibTableRow
hpnicfVsiIfEntry=_HpnicfVsiIfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,9,1))
hpnicfVsiIfEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:hpnicfVsiIfEntry.setStatus(_A)
_HpnicfVsiIfID_Type=Unsigned32
_HpnicfVsiIfID_Object=MibTableColumn
hpnicfVsiIfID=_HpnicfVsiIfID_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,9,1,1),_HpnicfVsiIfID_Type())
hpnicfVsiIfID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfVsiIfID.setStatus(_A)
_HpnicfVsiIfIndex_Type=InterfaceIndex
_HpnicfVsiIfIndex_Object=MibTableColumn
hpnicfVsiIfIndex=_HpnicfVsiIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,9,1,2),_HpnicfVsiIfIndex_Type())
hpnicfVsiIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVsiIfIndex.setStatus(_A)
_HpnicfVsiIfRowStatus_Type=RowStatus
_HpnicfVsiIfRowStatus_Object=MibTableColumn
hpnicfVsiIfRowStatus=_HpnicfVsiIfRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,105,1,9,1,3),_HpnicfVsiIfRowStatus_Type())
hpnicfVsiIfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVsiIfRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hpnicfVsi':hpnicfVsi,'hpnicfVsiObjects':hpnicfVsiObjects,'hpnicfVsiScalarGroup':hpnicfVsiScalarGroup,'hpnicfVsiNextAvailableVsiIndex':hpnicfVsiNextAvailableVsiIndex,'hpnicfVsiL2vpnStatus':hpnicfVsiL2vpnStatus,'hpnicfVsiTable':hpnicfVsiTable,'hpnicfVsiEntry':hpnicfVsiEntry,_G:hpnicfVsiIndex,'hpnicfVsiName':hpnicfVsiName,'hpnicfVsiMode':hpnicfVsiMode,'hpnicfMinmIsid':hpnicfMinmIsid,'hpnicfVsiId':hpnicfVsiId,'hpnicfVsiTransMode':hpnicfVsiTransMode,'hpnicfVsiEnableHubSpoke':hpnicfVsiEnableHubSpoke,'hpnicfVsiAdminState':hpnicfVsiAdminState,'hpnicfVsiRowStatus':hpnicfVsiRowStatus,'hpnicfVsiSpbIsid':hpnicfVsiSpbIsid,'hpnicfVsiVxlanID':hpnicfVsiVxlanID,'hpnicfVsiArpSuppression':hpnicfVsiArpSuppression,'hpnicfVsiFlooding':hpnicfVsiFlooding,'hpnicfVsiLocalMacCount':hpnicfVsiLocalMacCount,'hpnicfVsiInterfaceID':hpnicfVsiInterfaceID,'hpnicfVsiStatistics':hpnicfVsiStatistics,'hpnicfVsiNvgreID':hpnicfVsiNvgreID,'hpnicfVsiXconnectTable':hpnicfVsiXconnectTable,'hpnicfVsiXconnectEntry':hpnicfVsiXconnectEntry,_K:hpnicfVsiXconnectIfIndex,_L:hpnicfVsiXconnectEvcSrvInstId,'hpnicfVsiXconnectVsiName':hpnicfVsiXconnectVsiName,'hpnicfVsiXconnectAccessMode':hpnicfVsiXconnectAccessMode,'hpnicfVsiXconnectHubSpoke':hpnicfVsiXconnectHubSpoke,'hpnicfVsiXconnectRowStatus':hpnicfVsiXconnectRowStatus,'hpnicfVsiPwBindTable':hpnicfVsiPwBindTable,'hpnicfVsiPwBindEntry':hpnicfVsiPwBindEntry,_M:hpnicfVsiPwIndex,'hpnicfVsiPwBindAttributes':hpnicfVsiPwBindAttributes,'hpnicfVsiPwBindRowStatus':hpnicfVsiPwBindRowStatus,'hpnicfVsiFloodMacTable':hpnicfVsiFloodMacTable,'hpnicfVsiFloodMacEntry':hpnicfVsiFloodMacEntry,_N:hpnicfVsiFloodMac,'hpnicfVsiFloodMacRowStatus':hpnicfVsiFloodMacRowStatus,'hpnicfVsiLocalMacTable':hpnicfVsiLocalMacTable,'hpnicfVsiLocalMacEntry':hpnicfVsiLocalMacEntry,_O:hpnicfVsiLocalMacAddr,'hpnicfVsiLocalMacIfIndex':hpnicfVsiLocalMacIfIndex,'hpnicfVsiLocalMacSrvID':hpnicfVsiLocalMacSrvID,'hpnicfVsiPerfTable':hpnicfVsiPerfTable,'hpnicfVsiPerfEntry':hpnicfVsiPerfEntry,'hpnicfVsiPerfInOctets':hpnicfVsiPerfInOctets,'hpnicfVsiPerfInPackets':hpnicfVsiPerfInPackets,'hpnicfVsiPerfInErrors':hpnicfVsiPerfInErrors,'hpnicfVsiPerfInDiscards':hpnicfVsiPerfInDiscards,'hpnicfVsiPerfOutOctets':hpnicfVsiPerfOutOctets,'hpnicfVsiPerfOutPackets':hpnicfVsiPerfOutPackets,'hpnicfVsiPerfOutErrors':hpnicfVsiPerfOutErrors,'hpnicfVsiPerfOutDiscards':hpnicfVsiPerfOutDiscards,'hpnicfVsiNextAvailableVsiIfID':hpnicfVsiNextAvailableVsiIfID,'hpnicfVsiIfTable':hpnicfVsiIfTable,'hpnicfVsiIfEntry':hpnicfVsiIfEntry,_P:hpnicfVsiIfID,'hpnicfVsiIfIndex':hpnicfVsiIfIndex,'hpnicfVsiIfRowStatus':hpnicfVsiIfRowStatus})