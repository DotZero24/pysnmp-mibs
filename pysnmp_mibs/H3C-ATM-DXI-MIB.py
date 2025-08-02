_X='h3cAtmDxiGeneralGroup'
_W='h3cPVCMAPGroup'
_V='h3cAtmDxiConfMode'
_U='h3cAtmDxiMapRowStatus'
_T='h3cAtmDxiMapInarpTime'
_S='h3cAtmDxiMapBroEnable'
_R='h3cAtmDxiPvcRowStatus'
_Q='h3cAtmDxiPvcMapCount'
_P='h3cAtmDxiPvcEncType'
_O='h3cAtmDxiPvcDFA'
_N='h3cAtmDxiMapType'
_M='h3cAtmDxiMapPvcVci'
_L='h3cAtmDxiMapPvcVpi'
_K='h3cAtmDxiMapPeerIp'
_J='h3cAtmDxiMapPeerIpType'
_I='h3cAtmDxiPvcVci'
_H='h3cAtmDxiPvcVpi'
_G='ifIndex'
_F='IF-MIB'
_E='read-create'
_D='not-accessible'
_C='Integer32'
_B='H3C-ATM-DXI-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ifIndex,=mibBuilder.importSymbols(_F,_G)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
h3cAtmDxi=ModuleIdentity((1,3,6,1,4,1,2011,10,2,49))
if mibBuilder.loadTexts:h3cAtmDxi.setRevisions(('2005-04-14 15:18',))
_H3cAtmDxiScalarGroup_ObjectIdentity=ObjectIdentity
h3cAtmDxiScalarGroup=_H3cAtmDxiScalarGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,49,1))
class _H3cAtmDxiConfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mode1a',1),('mode1b',2),('mode2',3)))
_H3cAtmDxiConfMode_Type.__name__=_C
_H3cAtmDxiConfMode_Object=MibScalar
h3cAtmDxiConfMode=_H3cAtmDxiConfMode_Object((1,3,6,1,4,1,2011,10,2,49,1,1),_H3cAtmDxiConfMode_Type())
h3cAtmDxiConfMode.setMaxAccess('read-only')
if mibBuilder.loadTexts:h3cAtmDxiConfMode.setStatus(_A)
_H3cAtmDxiIfObjects_ObjectIdentity=ObjectIdentity
h3cAtmDxiIfObjects=_H3cAtmDxiIfObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,49,2))
_H3cAtmDxiPvcTable_Object=MibTable
h3cAtmDxiPvcTable=_H3cAtmDxiPvcTable_Object((1,3,6,1,4,1,2011,10,2,49,2,1))
if mibBuilder.loadTexts:h3cAtmDxiPvcTable.setStatus(_A)
_H3cAtmDxiPvcEntry_Object=MibTableRow
h3cAtmDxiPvcEntry=_H3cAtmDxiPvcEntry_Object((1,3,6,1,4,1,2011,10,2,49,2,1,1))
h3cAtmDxiPvcEntry.setIndexNames((0,_F,_G),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:h3cAtmDxiPvcEntry.setStatus(_A)
class _H3cAtmDxiPvcVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_H3cAtmDxiPvcVpi_Type.__name__=_C
_H3cAtmDxiPvcVpi_Object=MibTableColumn
h3cAtmDxiPvcVpi=_H3cAtmDxiPvcVpi_Object((1,3,6,1,4,1,2011,10,2,49,2,1,1,1),_H3cAtmDxiPvcVpi_Type())
h3cAtmDxiPvcVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cAtmDxiPvcVpi.setStatus(_A)
class _H3cAtmDxiPvcVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_H3cAtmDxiPvcVci_Type.__name__=_C
_H3cAtmDxiPvcVci_Object=MibTableColumn
h3cAtmDxiPvcVci=_H3cAtmDxiPvcVci_Object((1,3,6,1,4,1,2011,10,2,49,2,1,1,2),_H3cAtmDxiPvcVci_Type())
h3cAtmDxiPvcVci.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cAtmDxiPvcVci.setStatus(_A)
_H3cAtmDxiPvcDFA_Type=Integer32
_H3cAtmDxiPvcDFA_Object=MibTableColumn
h3cAtmDxiPvcDFA=_H3cAtmDxiPvcDFA_Object((1,3,6,1,4,1,2011,10,2,49,2,1,1,3),_H3cAtmDxiPvcDFA_Type())
h3cAtmDxiPvcDFA.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cAtmDxiPvcDFA.setStatus(_A)
class _H3cAtmDxiPvcEncType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('snap',1),('nlpid',2),('mux',3)))
_H3cAtmDxiPvcEncType_Type.__name__=_C
_H3cAtmDxiPvcEncType_Object=MibTableColumn
h3cAtmDxiPvcEncType=_H3cAtmDxiPvcEncType_Object((1,3,6,1,4,1,2011,10,2,49,2,1,1,4),_H3cAtmDxiPvcEncType_Type())
h3cAtmDxiPvcEncType.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cAtmDxiPvcEncType.setStatus(_A)
class _H3cAtmDxiPvcMapCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_H3cAtmDxiPvcMapCount_Type.__name__=_C
_H3cAtmDxiPvcMapCount_Object=MibTableColumn
h3cAtmDxiPvcMapCount=_H3cAtmDxiPvcMapCount_Object((1,3,6,1,4,1,2011,10,2,49,2,1,1,5),_H3cAtmDxiPvcMapCount_Type())
h3cAtmDxiPvcMapCount.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cAtmDxiPvcMapCount.setStatus(_A)
_H3cAtmDxiPvcRowStatus_Type=RowStatus
_H3cAtmDxiPvcRowStatus_Object=MibTableColumn
h3cAtmDxiPvcRowStatus=_H3cAtmDxiPvcRowStatus_Object((1,3,6,1,4,1,2011,10,2,49,2,1,1,6),_H3cAtmDxiPvcRowStatus_Type())
h3cAtmDxiPvcRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cAtmDxiPvcRowStatus.setStatus(_A)
_H3cAtmDxiMapTable_Object=MibTable
h3cAtmDxiMapTable=_H3cAtmDxiMapTable_Object((1,3,6,1,4,1,2011,10,2,49,2,2))
if mibBuilder.loadTexts:h3cAtmDxiMapTable.setStatus(_A)
_H3cAtmDxiMapEntry_Object=MibTableRow
h3cAtmDxiMapEntry=_H3cAtmDxiMapEntry_Object((1,3,6,1,4,1,2011,10,2,49,2,2,1))
h3cAtmDxiMapEntry.setIndexNames((0,_F,_G),(0,_B,_J),(0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:h3cAtmDxiMapEntry.setStatus(_A)
_H3cAtmDxiMapPeerIpType_Type=InetAddressType
_H3cAtmDxiMapPeerIpType_Object=MibTableColumn
h3cAtmDxiMapPeerIpType=_H3cAtmDxiMapPeerIpType_Object((1,3,6,1,4,1,2011,10,2,49,2,2,1,1),_H3cAtmDxiMapPeerIpType_Type())
h3cAtmDxiMapPeerIpType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cAtmDxiMapPeerIpType.setStatus(_A)
_H3cAtmDxiMapPeerIp_Type=InetAddress
_H3cAtmDxiMapPeerIp_Object=MibTableColumn
h3cAtmDxiMapPeerIp=_H3cAtmDxiMapPeerIp_Object((1,3,6,1,4,1,2011,10,2,49,2,2,1,2),_H3cAtmDxiMapPeerIp_Type())
h3cAtmDxiMapPeerIp.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cAtmDxiMapPeerIp.setStatus(_A)
class _H3cAtmDxiMapPvcVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_H3cAtmDxiMapPvcVpi_Type.__name__=_C
_H3cAtmDxiMapPvcVpi_Object=MibTableColumn
h3cAtmDxiMapPvcVpi=_H3cAtmDxiMapPvcVpi_Object((1,3,6,1,4,1,2011,10,2,49,2,2,1,3),_H3cAtmDxiMapPvcVpi_Type())
h3cAtmDxiMapPvcVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cAtmDxiMapPvcVpi.setStatus(_A)
class _H3cAtmDxiMapPvcVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_H3cAtmDxiMapPvcVci_Type.__name__=_C
_H3cAtmDxiMapPvcVci_Object=MibTableColumn
h3cAtmDxiMapPvcVci=_H3cAtmDxiMapPvcVci_Object((1,3,6,1,4,1,2011,10,2,49,2,2,1,4),_H3cAtmDxiMapPvcVci_Type())
h3cAtmDxiMapPvcVci.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cAtmDxiMapPvcVci.setStatus(_A)
class _H3cAtmDxiMapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('address',1),('inarp',2),('default',3)))
_H3cAtmDxiMapType_Type.__name__=_C
_H3cAtmDxiMapType_Object=MibTableColumn
h3cAtmDxiMapType=_H3cAtmDxiMapType_Object((1,3,6,1,4,1,2011,10,2,49,2,2,1,5),_H3cAtmDxiMapType_Type())
h3cAtmDxiMapType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cAtmDxiMapType.setStatus(_A)
class _H3cAtmDxiMapInarpTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5,10))
_H3cAtmDxiMapInarpTime_Type.__name__=_C
_H3cAtmDxiMapInarpTime_Object=MibTableColumn
h3cAtmDxiMapInarpTime=_H3cAtmDxiMapInarpTime_Object((1,3,6,1,4,1,2011,10,2,49,2,2,1,6),_H3cAtmDxiMapInarpTime_Type())
h3cAtmDxiMapInarpTime.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cAtmDxiMapInarpTime.setStatus(_A)
class _H3cAtmDxiMapBroEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_H3cAtmDxiMapBroEnable_Type.__name__=_C
_H3cAtmDxiMapBroEnable_Object=MibTableColumn
h3cAtmDxiMapBroEnable=_H3cAtmDxiMapBroEnable_Object((1,3,6,1,4,1,2011,10,2,49,2,2,1,7),_H3cAtmDxiMapBroEnable_Type())
h3cAtmDxiMapBroEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cAtmDxiMapBroEnable.setStatus(_A)
_H3cAtmDxiMapRowStatus_Type=RowStatus
_H3cAtmDxiMapRowStatus_Object=MibTableColumn
h3cAtmDxiMapRowStatus=_H3cAtmDxiMapRowStatus_Object((1,3,6,1,4,1,2011,10,2,49,2,2,1,8),_H3cAtmDxiMapRowStatus_Type())
h3cAtmDxiMapRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cAtmDxiMapRowStatus.setStatus(_A)
_H3cAtmDxiConformance_ObjectIdentity=ObjectIdentity
h3cAtmDxiConformance=_H3cAtmDxiConformance_ObjectIdentity((1,3,6,1,4,1,2011,10,2,49,3))
_H3cAtmDxiCompliances_ObjectIdentity=ObjectIdentity
h3cAtmDxiCompliances=_H3cAtmDxiCompliances_ObjectIdentity((1,3,6,1,4,1,2011,10,2,49,3,1))
_H3cAtmDxiGroup_ObjectIdentity=ObjectIdentity
h3cAtmDxiGroup=_H3cAtmDxiGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,49,3,2))
h3cPVCMAPGroup=ObjectGroup((1,3,6,1,4,1,2011,10,2,49,3,2,1))
h3cPVCMAPGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:h3cPVCMAPGroup.setStatus(_A)
h3cAtmDxiGeneralGroup=ObjectGroup((1,3,6,1,4,1,2011,10,2,49,3,2,2))
h3cAtmDxiGeneralGroup.setObjects((_B,_V))
if mibBuilder.loadTexts:h3cAtmDxiGeneralGroup.setStatus(_A)
h3cAtmDxiCompliance=ModuleCompliance((1,3,6,1,4,1,2011,10,2,49,3,1,1))
h3cAtmDxiCompliance.setObjects(*((_B,_W),(_B,_X)))
if mibBuilder.loadTexts:h3cAtmDxiCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cAtmDxi':h3cAtmDxi,'h3cAtmDxiScalarGroup':h3cAtmDxiScalarGroup,_V:h3cAtmDxiConfMode,'h3cAtmDxiIfObjects':h3cAtmDxiIfObjects,'h3cAtmDxiPvcTable':h3cAtmDxiPvcTable,'h3cAtmDxiPvcEntry':h3cAtmDxiPvcEntry,_H:h3cAtmDxiPvcVpi,_I:h3cAtmDxiPvcVci,_O:h3cAtmDxiPvcDFA,_P:h3cAtmDxiPvcEncType,_Q:h3cAtmDxiPvcMapCount,_R:h3cAtmDxiPvcRowStatus,'h3cAtmDxiMapTable':h3cAtmDxiMapTable,'h3cAtmDxiMapEntry':h3cAtmDxiMapEntry,_J:h3cAtmDxiMapPeerIpType,_K:h3cAtmDxiMapPeerIp,_L:h3cAtmDxiMapPvcVpi,_M:h3cAtmDxiMapPvcVci,_N:h3cAtmDxiMapType,_T:h3cAtmDxiMapInarpTime,_S:h3cAtmDxiMapBroEnable,_U:h3cAtmDxiMapRowStatus,'h3cAtmDxiConformance':h3cAtmDxiConformance,'h3cAtmDxiCompliances':h3cAtmDxiCompliances,'h3cAtmDxiCompliance':h3cAtmDxiCompliance,'h3cAtmDxiGroup':h3cAtmDxiGroup,_W:h3cPVCMAPGroup,_X:h3cAtmDxiGeneralGroup})