_I='pdnDot1dTpFdbVnidId'
_H='pdnDot1dTpFdbAddress'
_G='read-write'
_F='ifIndex'
_E='IF-MIB'
_D='PDN-BRIDGE-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
pdn_bridge,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-bridge')
VnidRange,=mibBuilder.importSymbols('PDN-TC','VnidRange')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
_PdnBridgeGenericMIBObjects_ObjectIdentity=ObjectIdentity
pdnBridgeGenericMIBObjects=_PdnBridgeGenericMIBObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,21,1))
_PdnDot1dGenericBridge_ObjectIdentity=ObjectIdentity
pdnDot1dGenericBridge=_PdnDot1dGenericBridge_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,21,1,1))
_PdnDot1dBaseBridgeAddress_Type=MacAddress
_PdnDot1dBaseBridgeAddress_Object=MibScalar
pdnDot1dBaseBridgeAddress=_PdnDot1dBaseBridgeAddress_Object((1,3,6,1,4,1,1795,2,24,2,21,1,1,1),_PdnDot1dBaseBridgeAddress_Type())
pdnDot1dBaseBridgeAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnDot1dBaseBridgeAddress.setStatus(_A)
_PdnDot1dBaseNumPorts_Type=Integer32
_PdnDot1dBaseNumPorts_Object=MibScalar
pdnDot1dBaseNumPorts=_PdnDot1dBaseNumPorts_Object((1,3,6,1,4,1,1795,2,24,2,21,1,1,2),_PdnDot1dBaseNumPorts_Type())
pdnDot1dBaseNumPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnDot1dBaseNumPorts.setStatus(_A)
class _PdnDot1dBaseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('transparent-only',2),('sourceroute-only',3),('srt',4)))
_PdnDot1dBaseType_Type.__name__=_C
_PdnDot1dBaseType_Object=MibScalar
pdnDot1dBaseType=_PdnDot1dBaseType_Object((1,3,6,1,4,1,1795,2,24,2,21,1,1,3),_PdnDot1dBaseType_Type())
pdnDot1dBaseType.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnDot1dBaseType.setStatus(_A)
_PdnDot1dTpLearnedEntryDiscards_Type=Counter32
_PdnDot1dTpLearnedEntryDiscards_Object=MibScalar
pdnDot1dTpLearnedEntryDiscards=_PdnDot1dTpLearnedEntryDiscards_Object((1,3,6,1,4,1,1795,2,24,2,21,1,1,4),_PdnDot1dTpLearnedEntryDiscards_Type())
pdnDot1dTpLearnedEntryDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnDot1dTpLearnedEntryDiscards.setStatus(_A)
class _PdnDot1dTpAgeingTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000000))
_PdnDot1dTpAgeingTime_Type.__name__=_C
_PdnDot1dTpAgeingTime_Object=MibScalar
pdnDot1dTpAgeingTime=_PdnDot1dTpAgeingTime_Object((1,3,6,1,4,1,1795,2,24,2,21,1,1,5),_PdnDot1dTpAgeingTime_Type())
pdnDot1dTpAgeingTime.setMaxAccess(_G)
if mibBuilder.loadTexts:pdnDot1dTpAgeingTime.setStatus(_A)
class _PdnDot1dTpAgeingCleanupTime_Type(Integer32):defaultValue=150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,500000))
_PdnDot1dTpAgeingCleanupTime_Type.__name__=_C
_PdnDot1dTpAgeingCleanupTime_Object=MibScalar
pdnDot1dTpAgeingCleanupTime=_PdnDot1dTpAgeingCleanupTime_Object((1,3,6,1,4,1,1795,2,24,2,21,1,1,6),_PdnDot1dTpAgeingCleanupTime_Type())
pdnDot1dTpAgeingCleanupTime.setMaxAccess(_G)
if mibBuilder.loadTexts:pdnDot1dTpAgeingCleanupTime.setStatus(_A)
_PdnDot1dTpFdb_ObjectIdentity=ObjectIdentity
pdnDot1dTpFdb=_PdnDot1dTpFdb_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,21,1,2))
_PdnDot1dTpFdbTable_Object=MibTable
pdnDot1dTpFdbTable=_PdnDot1dTpFdbTable_Object((1,3,6,1,4,1,1795,2,24,2,21,1,2,1))
if mibBuilder.loadTexts:pdnDot1dTpFdbTable.setStatus(_A)
_PdnDot1dTpFdbEntry_Object=MibTableRow
pdnDot1dTpFdbEntry=_PdnDot1dTpFdbEntry_Object((1,3,6,1,4,1,1795,2,24,2,21,1,2,1,1))
pdnDot1dTpFdbEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:pdnDot1dTpFdbEntry.setStatus(_A)
_PdnDot1dTpFdbAddress_Type=MacAddress
_PdnDot1dTpFdbAddress_Object=MibTableColumn
pdnDot1dTpFdbAddress=_PdnDot1dTpFdbAddress_Object((1,3,6,1,4,1,1795,2,24,2,21,1,2,1,1,1),_PdnDot1dTpFdbAddress_Type())
pdnDot1dTpFdbAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnDot1dTpFdbAddress.setStatus(_A)
_PdnDot1dTpFdbVnidId_Type=VnidRange
_PdnDot1dTpFdbVnidId_Object=MibTableColumn
pdnDot1dTpFdbVnidId=_PdnDot1dTpFdbVnidId_Object((1,3,6,1,4,1,1795,2,24,2,21,1,2,1,1,2),_PdnDot1dTpFdbVnidId_Type())
pdnDot1dTpFdbVnidId.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnDot1dTpFdbVnidId.setStatus(_A)
_PdnDot1dTpFdbIfIndex_Type=Integer32
_PdnDot1dTpFdbIfIndex_Object=MibTableColumn
pdnDot1dTpFdbIfIndex=_PdnDot1dTpFdbIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,21,1,2,1,1,3),_PdnDot1dTpFdbIfIndex_Type())
pdnDot1dTpFdbIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnDot1dTpFdbIfIndex.setStatus(_A)
class _PdnDot1dTpFdbStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('invalid',2),('learned',3),('self',4),('mgmt',5)))
_PdnDot1dTpFdbStatus_Type.__name__=_C
_PdnDot1dTpFdbStatus_Object=MibTableColumn
pdnDot1dTpFdbStatus=_PdnDot1dTpFdbStatus_Object((1,3,6,1,4,1,1795,2,24,2,21,1,2,1,1,4),_PdnDot1dTpFdbStatus_Type())
pdnDot1dTpFdbStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnDot1dTpFdbStatus.setStatus(_A)
_PdnDot1dTpFdbAgeTime_Type=Integer32
_PdnDot1dTpFdbAgeTime_Object=MibTableColumn
pdnDot1dTpFdbAgeTime=_PdnDot1dTpFdbAgeTime_Object((1,3,6,1,4,1,1795,2,24,2,21,1,2,1,1,5),_PdnDot1dTpFdbAgeTime_Type())
pdnDot1dTpFdbAgeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnDot1dTpFdbAgeTime.setStatus(_A)
class _PdnDot1dTpFdbFlags_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('permanentDHCP',2),('permanentCONFIGURED',3),('dynamic',4)))
_PdnDot1dTpFdbFlags_Type.__name__=_C
_PdnDot1dTpFdbFlags_Object=MibTableColumn
pdnDot1dTpFdbFlags=_PdnDot1dTpFdbFlags_Object((1,3,6,1,4,1,1795,2,24,2,21,1,2,1,1,6),_PdnDot1dTpFdbFlags_Type())
pdnDot1dTpFdbFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnDot1dTpFdbFlags.setStatus(_A)
_PdnDot1dTp_ObjectIdentity=ObjectIdentity
pdnDot1dTp=_PdnDot1dTp_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,21,1,3))
_PdnDot1dTpPortTable_Object=MibTable
pdnDot1dTpPortTable=_PdnDot1dTpPortTable_Object((1,3,6,1,4,1,1795,2,24,2,21,1,3,1))
if mibBuilder.loadTexts:pdnDot1dTpPortTable.setStatus(_A)
_PdnDot1dTpPortEntry_Object=MibTableRow
pdnDot1dTpPortEntry=_PdnDot1dTpPortEntry_Object((1,3,6,1,4,1,1795,2,24,2,21,1,3,1,1))
pdnDot1dTpPortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:pdnDot1dTpPortEntry.setStatus(_A)
_PdnDot1dTpPortMaxInfo_Type=Integer32
_PdnDot1dTpPortMaxInfo_Object=MibTableColumn
pdnDot1dTpPortMaxInfo=_PdnDot1dTpPortMaxInfo_Object((1,3,6,1,4,1,1795,2,24,2,21,1,3,1,1,1),_PdnDot1dTpPortMaxInfo_Type())
pdnDot1dTpPortMaxInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnDot1dTpPortMaxInfo.setStatus(_A)
_PdnDot1dTpPortInFrames_Type=Counter32
_PdnDot1dTpPortInFrames_Object=MibTableColumn
pdnDot1dTpPortInFrames=_PdnDot1dTpPortInFrames_Object((1,3,6,1,4,1,1795,2,24,2,21,1,3,1,1,2),_PdnDot1dTpPortInFrames_Type())
pdnDot1dTpPortInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnDot1dTpPortInFrames.setStatus(_A)
_PdnDot1dTpPortOutFrames_Type=Counter32
_PdnDot1dTpPortOutFrames_Object=MibTableColumn
pdnDot1dTpPortOutFrames=_PdnDot1dTpPortOutFrames_Object((1,3,6,1,4,1,1795,2,24,2,21,1,3,1,1,3),_PdnDot1dTpPortOutFrames_Type())
pdnDot1dTpPortOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnDot1dTpPortOutFrames.setStatus(_A)
_PdnDot1dTpPortInDiscards_Type=Counter32
_PdnDot1dTpPortInDiscards_Object=MibTableColumn
pdnDot1dTpPortInDiscards=_PdnDot1dTpPortInDiscards_Object((1,3,6,1,4,1,1795,2,24,2,21,1,3,1,1,4),_PdnDot1dTpPortInDiscards_Type())
pdnDot1dTpPortInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnDot1dTpPortInDiscards.setStatus(_A)
_PdnBridgeMIBTraps_ObjectIdentity=ObjectIdentity
pdnBridgeMIBTraps=_PdnBridgeMIBTraps_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,21,2))
mibBuilder.exportSymbols(_D,**{'pdnBridgeGenericMIBObjects':pdnBridgeGenericMIBObjects,'pdnDot1dGenericBridge':pdnDot1dGenericBridge,'pdnDot1dBaseBridgeAddress':pdnDot1dBaseBridgeAddress,'pdnDot1dBaseNumPorts':pdnDot1dBaseNumPorts,'pdnDot1dBaseType':pdnDot1dBaseType,'pdnDot1dTpLearnedEntryDiscards':pdnDot1dTpLearnedEntryDiscards,'pdnDot1dTpAgeingTime':pdnDot1dTpAgeingTime,'pdnDot1dTpAgeingCleanupTime':pdnDot1dTpAgeingCleanupTime,'pdnDot1dTpFdb':pdnDot1dTpFdb,'pdnDot1dTpFdbTable':pdnDot1dTpFdbTable,'pdnDot1dTpFdbEntry':pdnDot1dTpFdbEntry,_H:pdnDot1dTpFdbAddress,_I:pdnDot1dTpFdbVnidId,'pdnDot1dTpFdbIfIndex':pdnDot1dTpFdbIfIndex,'pdnDot1dTpFdbStatus':pdnDot1dTpFdbStatus,'pdnDot1dTpFdbAgeTime':pdnDot1dTpFdbAgeTime,'pdnDot1dTpFdbFlags':pdnDot1dTpFdbFlags,'pdnDot1dTp':pdnDot1dTp,'pdnDot1dTpPortTable':pdnDot1dTpPortTable,'pdnDot1dTpPortEntry':pdnDot1dTpPortEntry,'pdnDot1dTpPortMaxInfo':pdnDot1dTpPortMaxInfo,'pdnDot1dTpPortInFrames':pdnDot1dTpPortInFrames,'pdnDot1dTpPortOutFrames':pdnDot1dTpPortOutFrames,'pdnDot1dTpPortInDiscards':pdnDot1dTpPortInDiscards,'pdnBridgeMIBTraps':pdnBridgeMIBTraps})