_X='hpnicfAtmDxiGeneralGroup'
_W='hpnicfPVCMAPGroup'
_V='hpnicfAtmDxiConfMode'
_U='hpnicfAtmDxiMapRowStatus'
_T='hpnicfAtmDxiMapInarpTime'
_S='hpnicfAtmDxiMapBroEnable'
_R='hpnicfAtmDxiPvcRowStatus'
_Q='hpnicfAtmDxiPvcMapCount'
_P='hpnicfAtmDxiPvcEncType'
_O='hpnicfAtmDxiPvcDFA'
_N='hpnicfAtmDxiMapType'
_M='hpnicfAtmDxiMapPvcVci'
_L='hpnicfAtmDxiMapPvcVpi'
_K='hpnicfAtmDxiMapPeerIp'
_J='hpnicfAtmDxiMapPeerIpType'
_I='hpnicfAtmDxiPvcVci'
_H='hpnicfAtmDxiPvcVpi'
_G='ifIndex'
_F='IF-MIB'
_E='read-create'
_D='not-accessible'
_C='Integer32'
_B='HPN-ICF-ATM-DXI-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifIndex,=mibBuilder.importSymbols(_F,_G)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfAtmDxi=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,49))
if mibBuilder.loadTexts:hpnicfAtmDxi.setRevisions(('2005-04-14 15:18',))
_HpnicfAtmDxiScalarGroup_ObjectIdentity=ObjectIdentity
hpnicfAtmDxiScalarGroup=_HpnicfAtmDxiScalarGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,49,1))
class _HpnicfAtmDxiConfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mode1a',1),('mode1b',2),('mode2',3)))
_HpnicfAtmDxiConfMode_Type.__name__=_C
_HpnicfAtmDxiConfMode_Object=MibScalar
hpnicfAtmDxiConfMode=_HpnicfAtmDxiConfMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,49,1,1),_HpnicfAtmDxiConfMode_Type())
hpnicfAtmDxiConfMode.setMaxAccess('read-only')
if mibBuilder.loadTexts:hpnicfAtmDxiConfMode.setStatus(_A)
_HpnicfAtmDxiIfObjects_ObjectIdentity=ObjectIdentity
hpnicfAtmDxiIfObjects=_HpnicfAtmDxiIfObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,49,2))
_HpnicfAtmDxiPvcTable_Object=MibTable
hpnicfAtmDxiPvcTable=_HpnicfAtmDxiPvcTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,49,2,1))
if mibBuilder.loadTexts:hpnicfAtmDxiPvcTable.setStatus(_A)
_HpnicfAtmDxiPvcEntry_Object=MibTableRow
hpnicfAtmDxiPvcEntry=_HpnicfAtmDxiPvcEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,49,2,1,1))
hpnicfAtmDxiPvcEntry.setIndexNames((0,_F,_G),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:hpnicfAtmDxiPvcEntry.setStatus(_A)
class _HpnicfAtmDxiPvcVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_HpnicfAtmDxiPvcVpi_Type.__name__=_C
_HpnicfAtmDxiPvcVpi_Object=MibTableColumn
hpnicfAtmDxiPvcVpi=_HpnicfAtmDxiPvcVpi_Object((1,3,6,1,4,1,11,2,14,11,15,2,49,2,1,1,1),_HpnicfAtmDxiPvcVpi_Type())
hpnicfAtmDxiPvcVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfAtmDxiPvcVpi.setStatus(_A)
class _HpnicfAtmDxiPvcVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HpnicfAtmDxiPvcVci_Type.__name__=_C
_HpnicfAtmDxiPvcVci_Object=MibTableColumn
hpnicfAtmDxiPvcVci=_HpnicfAtmDxiPvcVci_Object((1,3,6,1,4,1,11,2,14,11,15,2,49,2,1,1,2),_HpnicfAtmDxiPvcVci_Type())
hpnicfAtmDxiPvcVci.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfAtmDxiPvcVci.setStatus(_A)
_HpnicfAtmDxiPvcDFA_Type=Integer32
_HpnicfAtmDxiPvcDFA_Object=MibTableColumn
hpnicfAtmDxiPvcDFA=_HpnicfAtmDxiPvcDFA_Object((1,3,6,1,4,1,11,2,14,11,15,2,49,2,1,1,3),_HpnicfAtmDxiPvcDFA_Type())
hpnicfAtmDxiPvcDFA.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfAtmDxiPvcDFA.setStatus(_A)
class _HpnicfAtmDxiPvcEncType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('snap',1),('nlpid',2),('mux',3)))
_HpnicfAtmDxiPvcEncType_Type.__name__=_C
_HpnicfAtmDxiPvcEncType_Object=MibTableColumn
hpnicfAtmDxiPvcEncType=_HpnicfAtmDxiPvcEncType_Object((1,3,6,1,4,1,11,2,14,11,15,2,49,2,1,1,4),_HpnicfAtmDxiPvcEncType_Type())
hpnicfAtmDxiPvcEncType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfAtmDxiPvcEncType.setStatus(_A)
class _HpnicfAtmDxiPvcMapCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_HpnicfAtmDxiPvcMapCount_Type.__name__=_C
_HpnicfAtmDxiPvcMapCount_Object=MibTableColumn
hpnicfAtmDxiPvcMapCount=_HpnicfAtmDxiPvcMapCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,49,2,1,1,5),_HpnicfAtmDxiPvcMapCount_Type())
hpnicfAtmDxiPvcMapCount.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfAtmDxiPvcMapCount.setStatus(_A)
_HpnicfAtmDxiPvcRowStatus_Type=RowStatus
_HpnicfAtmDxiPvcRowStatus_Object=MibTableColumn
hpnicfAtmDxiPvcRowStatus=_HpnicfAtmDxiPvcRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,49,2,1,1,6),_HpnicfAtmDxiPvcRowStatus_Type())
hpnicfAtmDxiPvcRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfAtmDxiPvcRowStatus.setStatus(_A)
_HpnicfAtmDxiMapTable_Object=MibTable
hpnicfAtmDxiMapTable=_HpnicfAtmDxiMapTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,49,2,2))
if mibBuilder.loadTexts:hpnicfAtmDxiMapTable.setStatus(_A)
_HpnicfAtmDxiMapEntry_Object=MibTableRow
hpnicfAtmDxiMapEntry=_HpnicfAtmDxiMapEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,49,2,2,1))
hpnicfAtmDxiMapEntry.setIndexNames((0,_F,_G),(0,_B,_J),(0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:hpnicfAtmDxiMapEntry.setStatus(_A)
_HpnicfAtmDxiMapPeerIpType_Type=InetAddressType
_HpnicfAtmDxiMapPeerIpType_Object=MibTableColumn
hpnicfAtmDxiMapPeerIpType=_HpnicfAtmDxiMapPeerIpType_Object((1,3,6,1,4,1,11,2,14,11,15,2,49,2,2,1,1),_HpnicfAtmDxiMapPeerIpType_Type())
hpnicfAtmDxiMapPeerIpType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfAtmDxiMapPeerIpType.setStatus(_A)
_HpnicfAtmDxiMapPeerIp_Type=InetAddress
_HpnicfAtmDxiMapPeerIp_Object=MibTableColumn
hpnicfAtmDxiMapPeerIp=_HpnicfAtmDxiMapPeerIp_Object((1,3,6,1,4,1,11,2,14,11,15,2,49,2,2,1,2),_HpnicfAtmDxiMapPeerIp_Type())
hpnicfAtmDxiMapPeerIp.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfAtmDxiMapPeerIp.setStatus(_A)
class _HpnicfAtmDxiMapPvcVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_HpnicfAtmDxiMapPvcVpi_Type.__name__=_C
_HpnicfAtmDxiMapPvcVpi_Object=MibTableColumn
hpnicfAtmDxiMapPvcVpi=_HpnicfAtmDxiMapPvcVpi_Object((1,3,6,1,4,1,11,2,14,11,15,2,49,2,2,1,3),_HpnicfAtmDxiMapPvcVpi_Type())
hpnicfAtmDxiMapPvcVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfAtmDxiMapPvcVpi.setStatus(_A)
class _HpnicfAtmDxiMapPvcVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HpnicfAtmDxiMapPvcVci_Type.__name__=_C
_HpnicfAtmDxiMapPvcVci_Object=MibTableColumn
hpnicfAtmDxiMapPvcVci=_HpnicfAtmDxiMapPvcVci_Object((1,3,6,1,4,1,11,2,14,11,15,2,49,2,2,1,4),_HpnicfAtmDxiMapPvcVci_Type())
hpnicfAtmDxiMapPvcVci.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfAtmDxiMapPvcVci.setStatus(_A)
class _HpnicfAtmDxiMapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('address',1),('inarp',2),('default',3)))
_HpnicfAtmDxiMapType_Type.__name__=_C
_HpnicfAtmDxiMapType_Object=MibTableColumn
hpnicfAtmDxiMapType=_HpnicfAtmDxiMapType_Object((1,3,6,1,4,1,11,2,14,11,15,2,49,2,2,1,5),_HpnicfAtmDxiMapType_Type())
hpnicfAtmDxiMapType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfAtmDxiMapType.setStatus(_A)
class _HpnicfAtmDxiMapInarpTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5,10))
_HpnicfAtmDxiMapInarpTime_Type.__name__=_C
_HpnicfAtmDxiMapInarpTime_Object=MibTableColumn
hpnicfAtmDxiMapInarpTime=_HpnicfAtmDxiMapInarpTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,49,2,2,1,6),_HpnicfAtmDxiMapInarpTime_Type())
hpnicfAtmDxiMapInarpTime.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfAtmDxiMapInarpTime.setStatus(_A)
class _HpnicfAtmDxiMapBroEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HpnicfAtmDxiMapBroEnable_Type.__name__=_C
_HpnicfAtmDxiMapBroEnable_Object=MibTableColumn
hpnicfAtmDxiMapBroEnable=_HpnicfAtmDxiMapBroEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,49,2,2,1,7),_HpnicfAtmDxiMapBroEnable_Type())
hpnicfAtmDxiMapBroEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfAtmDxiMapBroEnable.setStatus(_A)
_HpnicfAtmDxiMapRowStatus_Type=RowStatus
_HpnicfAtmDxiMapRowStatus_Object=MibTableColumn
hpnicfAtmDxiMapRowStatus=_HpnicfAtmDxiMapRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,49,2,2,1,8),_HpnicfAtmDxiMapRowStatus_Type())
hpnicfAtmDxiMapRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfAtmDxiMapRowStatus.setStatus(_A)
_HpnicfAtmDxiConformance_ObjectIdentity=ObjectIdentity
hpnicfAtmDxiConformance=_HpnicfAtmDxiConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,49,3))
_HpnicfAtmDxiCompliances_ObjectIdentity=ObjectIdentity
hpnicfAtmDxiCompliances=_HpnicfAtmDxiCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,49,3,1))
_HpnicfAtmDxiGroup_ObjectIdentity=ObjectIdentity
hpnicfAtmDxiGroup=_HpnicfAtmDxiGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,49,3,2))
hpnicfPVCMAPGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,49,3,2,1))
hpnicfPVCMAPGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:hpnicfPVCMAPGroup.setStatus(_A)
hpnicfAtmDxiGeneralGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,49,3,2,2))
hpnicfAtmDxiGeneralGroup.setObjects((_B,_V))
if mibBuilder.loadTexts:hpnicfAtmDxiGeneralGroup.setStatus(_A)
hpnicfAtmDxiCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,2,49,3,1,1))
hpnicfAtmDxiCompliance.setObjects(*((_B,_W),(_B,_X)))
if mibBuilder.loadTexts:hpnicfAtmDxiCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfAtmDxi':hpnicfAtmDxi,'hpnicfAtmDxiScalarGroup':hpnicfAtmDxiScalarGroup,_V:hpnicfAtmDxiConfMode,'hpnicfAtmDxiIfObjects':hpnicfAtmDxiIfObjects,'hpnicfAtmDxiPvcTable':hpnicfAtmDxiPvcTable,'hpnicfAtmDxiPvcEntry':hpnicfAtmDxiPvcEntry,_H:hpnicfAtmDxiPvcVpi,_I:hpnicfAtmDxiPvcVci,_O:hpnicfAtmDxiPvcDFA,_P:hpnicfAtmDxiPvcEncType,_Q:hpnicfAtmDxiPvcMapCount,_R:hpnicfAtmDxiPvcRowStatus,'hpnicfAtmDxiMapTable':hpnicfAtmDxiMapTable,'hpnicfAtmDxiMapEntry':hpnicfAtmDxiMapEntry,_J:hpnicfAtmDxiMapPeerIpType,_K:hpnicfAtmDxiMapPeerIp,_L:hpnicfAtmDxiMapPvcVpi,_M:hpnicfAtmDxiMapPvcVci,_N:hpnicfAtmDxiMapType,_T:hpnicfAtmDxiMapInarpTime,_S:hpnicfAtmDxiMapBroEnable,_U:hpnicfAtmDxiMapRowStatus,'hpnicfAtmDxiConformance':hpnicfAtmDxiConformance,'hpnicfAtmDxiCompliances':hpnicfAtmDxiCompliances,'hpnicfAtmDxiCompliance':hpnicfAtmDxiCompliance,'hpnicfAtmDxiGroup':hpnicfAtmDxiGroup,_W:hpnicfPVCMAPGroup,_X:hpnicfAtmDxiGeneralGroup})