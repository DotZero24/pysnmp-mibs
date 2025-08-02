_K='hpnicfNvgreStaticMacAddr'
_J='hpnicfNvgreMacAddr'
_I='Integer32'
_H='hpnicfNvgreVsiIndex'
_G='hpnicfNvgreTunnelID'
_F='hpnicfNvgreID'
_E='not-accessible'
_D='read-create'
_C='read-only'
_B='HPN-ICF-NVGRE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
hpnicfNvgre=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,156))
if mibBuilder.loadTexts:hpnicfNvgre.setRevisions(('2014-03-11 09:00',))
_HpnicfNvgreObjects_ObjectIdentity=ObjectIdentity
hpnicfNvgreObjects=_HpnicfNvgreObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,156,1))
_HpnicfNvgreScalarGroup_ObjectIdentity=ObjectIdentity
hpnicfNvgreScalarGroup=_HpnicfNvgreScalarGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,156,1,1))
_HpnicfNvgreNextNvgreID_Type=Unsigned32
_HpnicfNvgreNextNvgreID_Object=MibScalar
hpnicfNvgreNextNvgreID=_HpnicfNvgreNextNvgreID_Object((1,3,6,1,4,1,11,2,14,11,15,2,156,1,1,1),_HpnicfNvgreNextNvgreID_Type())
hpnicfNvgreNextNvgreID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNvgreNextNvgreID.setStatus(_A)
_HpnicfNvgreConfigured_Type=Unsigned32
_HpnicfNvgreConfigured_Object=MibScalar
hpnicfNvgreConfigured=_HpnicfNvgreConfigured_Object((1,3,6,1,4,1,11,2,14,11,15,2,156,1,1,2),_HpnicfNvgreConfigured_Type())
hpnicfNvgreConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNvgreConfigured.setStatus(_A)
_HpnicfNvgreTable_Object=MibTable
hpnicfNvgreTable=_HpnicfNvgreTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,156,1,2))
if mibBuilder.loadTexts:hpnicfNvgreTable.setStatus(_A)
_HpnicfNvgreEntry_Object=MibTableRow
hpnicfNvgreEntry=_HpnicfNvgreEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,156,1,2,1))
hpnicfNvgreEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:hpnicfNvgreEntry.setStatus(_A)
_HpnicfNvgreID_Type=Unsigned32
_HpnicfNvgreID_Object=MibTableColumn
hpnicfNvgreID=_HpnicfNvgreID_Object((1,3,6,1,4,1,11,2,14,11,15,2,156,1,2,1,1),_HpnicfNvgreID_Type())
hpnicfNvgreID.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNvgreID.setStatus(_A)
_HpnicfNvgreVsiIndex_Type=Unsigned32
_HpnicfNvgreVsiIndex_Object=MibTableColumn
hpnicfNvgreVsiIndex=_HpnicfNvgreVsiIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,156,1,2,1,2),_HpnicfNvgreVsiIndex_Type())
hpnicfNvgreVsiIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfNvgreVsiIndex.setStatus(_A)
_HpnicfNvgreRemoteMacCount_Type=Unsigned32
_HpnicfNvgreRemoteMacCount_Object=MibTableColumn
hpnicfNvgreRemoteMacCount=_HpnicfNvgreRemoteMacCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,156,1,2,1,3),_HpnicfNvgreRemoteMacCount_Type())
hpnicfNvgreRemoteMacCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNvgreRemoteMacCount.setStatus(_A)
_HpnicfNvgreRowStatus_Type=RowStatus
_HpnicfNvgreRowStatus_Object=MibTableColumn
hpnicfNvgreRowStatus=_HpnicfNvgreRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,156,1,2,1,4),_HpnicfNvgreRowStatus_Type())
hpnicfNvgreRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfNvgreRowStatus.setStatus(_A)
_HpnicfNvgreTunnelTable_Object=MibTable
hpnicfNvgreTunnelTable=_HpnicfNvgreTunnelTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,156,1,3))
if mibBuilder.loadTexts:hpnicfNvgreTunnelTable.setStatus(_A)
_HpnicfNvgreTunnelEntry_Object=MibTableRow
hpnicfNvgreTunnelEntry=_HpnicfNvgreTunnelEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,156,1,3,1))
hpnicfNvgreTunnelEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfNvgreTunnelEntry.setStatus(_A)
_HpnicfNvgreTunnelID_Type=Unsigned32
_HpnicfNvgreTunnelID_Object=MibTableColumn
hpnicfNvgreTunnelID=_HpnicfNvgreTunnelID_Object((1,3,6,1,4,1,11,2,14,11,15,2,156,1,3,1,1),_HpnicfNvgreTunnelID_Type())
hpnicfNvgreTunnelID.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNvgreTunnelID.setStatus(_A)
_HpnicfNvgreTunnelRowStatus_Type=RowStatus
_HpnicfNvgreTunnelRowStatus_Object=MibTableColumn
hpnicfNvgreTunnelRowStatus=_HpnicfNvgreTunnelRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,156,1,3,1,2),_HpnicfNvgreTunnelRowStatus_Type())
hpnicfNvgreTunnelRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfNvgreTunnelRowStatus.setStatus(_A)
_HpnicfNvgreTunnelOctets_Type=Counter64
_HpnicfNvgreTunnelOctets_Object=MibTableColumn
hpnicfNvgreTunnelOctets=_HpnicfNvgreTunnelOctets_Object((1,3,6,1,4,1,11,2,14,11,15,2,156,1,3,1,3),_HpnicfNvgreTunnelOctets_Type())
hpnicfNvgreTunnelOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNvgreTunnelOctets.setStatus(_A)
_HpnicfNvgreTunnelPackets_Type=Counter64
_HpnicfNvgreTunnelPackets_Object=MibTableColumn
hpnicfNvgreTunnelPackets=_HpnicfNvgreTunnelPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,156,1,3,1,4),_HpnicfNvgreTunnelPackets_Type())
hpnicfNvgreTunnelPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNvgreTunnelPackets.setStatus(_A)
_HpnicfNvgreTunnelBoundTable_Object=MibTable
hpnicfNvgreTunnelBoundTable=_HpnicfNvgreTunnelBoundTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,156,1,4))
if mibBuilder.loadTexts:hpnicfNvgreTunnelBoundTable.setStatus(_A)
_HpnicfNvgreTunnelBoundEntry_Object=MibTableRow
hpnicfNvgreTunnelBoundEntry=_HpnicfNvgreTunnelBoundEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,156,1,4,1))
hpnicfNvgreTunnelBoundEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:hpnicfNvgreTunnelBoundEntry.setStatus(_A)
_HpnicfNvgreTunnelBoundNvgreNum_Type=Unsigned32
_HpnicfNvgreTunnelBoundNvgreNum_Object=MibTableColumn
hpnicfNvgreTunnelBoundNvgreNum=_HpnicfNvgreTunnelBoundNvgreNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,156,1,4,1,1),_HpnicfNvgreTunnelBoundNvgreNum_Type())
hpnicfNvgreTunnelBoundNvgreNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNvgreTunnelBoundNvgreNum.setStatus(_A)
_HpnicfNvgreMacTable_Object=MibTable
hpnicfNvgreMacTable=_HpnicfNvgreMacTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,156,1,5))
if mibBuilder.loadTexts:hpnicfNvgreMacTable.setStatus(_A)
_HpnicfNvgreMacEntry_Object=MibTableRow
hpnicfNvgreMacEntry=_HpnicfNvgreMacEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,156,1,5,1))
hpnicfNvgreMacEntry.setIndexNames((0,_B,_H),(0,_B,_J))
if mibBuilder.loadTexts:hpnicfNvgreMacEntry.setStatus(_A)
_HpnicfNvgreMacAddr_Type=MacAddress
_HpnicfNvgreMacAddr_Object=MibTableColumn
hpnicfNvgreMacAddr=_HpnicfNvgreMacAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,156,1,5,1,1),_HpnicfNvgreMacAddr_Type())
hpnicfNvgreMacAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNvgreMacAddr.setStatus(_A)
_HpnicfNvgreMacTunnelID_Type=Unsigned32
_HpnicfNvgreMacTunnelID_Object=MibTableColumn
hpnicfNvgreMacTunnelID=_HpnicfNvgreMacTunnelID_Object((1,3,6,1,4,1,11,2,14,11,15,2,156,1,5,1,2),_HpnicfNvgreMacTunnelID_Type())
hpnicfNvgreMacTunnelID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNvgreMacTunnelID.setStatus(_A)
class _HpnicfNvgreMacType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('selfLearned',1),('staticConfigured',2),('protocolLearned',3)))
_HpnicfNvgreMacType_Type.__name__=_I
_HpnicfNvgreMacType_Object=MibTableColumn
hpnicfNvgreMacType=_HpnicfNvgreMacType_Object((1,3,6,1,4,1,11,2,14,11,15,2,156,1,5,1,3),_HpnicfNvgreMacType_Type())
hpnicfNvgreMacType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNvgreMacType.setStatus(_A)
_HpnicfNvgreStaticMacTable_Object=MibTable
hpnicfNvgreStaticMacTable=_HpnicfNvgreStaticMacTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,156,1,6))
if mibBuilder.loadTexts:hpnicfNvgreStaticMacTable.setStatus(_A)
_HpnicfNvgreStaticMacEntry_Object=MibTableRow
hpnicfNvgreStaticMacEntry=_HpnicfNvgreStaticMacEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,156,1,6,1))
hpnicfNvgreStaticMacEntry.setIndexNames((0,_B,_H),(0,_B,_K))
if mibBuilder.loadTexts:hpnicfNvgreStaticMacEntry.setStatus(_A)
_HpnicfNvgreStaticMacAddr_Type=MacAddress
_HpnicfNvgreStaticMacAddr_Object=MibTableColumn
hpnicfNvgreStaticMacAddr=_HpnicfNvgreStaticMacAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,156,1,6,1,1),_HpnicfNvgreStaticMacAddr_Type())
hpnicfNvgreStaticMacAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNvgreStaticMacAddr.setStatus(_A)
_HpnicfNvgreStaticMacTunnelID_Type=Unsigned32
_HpnicfNvgreStaticMacTunnelID_Object=MibTableColumn
hpnicfNvgreStaticMacTunnelID=_HpnicfNvgreStaticMacTunnelID_Object((1,3,6,1,4,1,11,2,14,11,15,2,156,1,6,1,2),_HpnicfNvgreStaticMacTunnelID_Type())
hpnicfNvgreStaticMacTunnelID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfNvgreStaticMacTunnelID.setStatus(_A)
_HpnicfNvgreStaticMacRowStatus_Type=RowStatus
_HpnicfNvgreStaticMacRowStatus_Object=MibTableColumn
hpnicfNvgreStaticMacRowStatus=_HpnicfNvgreStaticMacRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,156,1,6,1,3),_HpnicfNvgreStaticMacRowStatus_Type())
hpnicfNvgreStaticMacRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfNvgreStaticMacRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfNvgre':hpnicfNvgre,'hpnicfNvgreObjects':hpnicfNvgreObjects,'hpnicfNvgreScalarGroup':hpnicfNvgreScalarGroup,'hpnicfNvgreNextNvgreID':hpnicfNvgreNextNvgreID,'hpnicfNvgreConfigured':hpnicfNvgreConfigured,'hpnicfNvgreTable':hpnicfNvgreTable,'hpnicfNvgreEntry':hpnicfNvgreEntry,_F:hpnicfNvgreID,_H:hpnicfNvgreVsiIndex,'hpnicfNvgreRemoteMacCount':hpnicfNvgreRemoteMacCount,'hpnicfNvgreRowStatus':hpnicfNvgreRowStatus,'hpnicfNvgreTunnelTable':hpnicfNvgreTunnelTable,'hpnicfNvgreTunnelEntry':hpnicfNvgreTunnelEntry,_G:hpnicfNvgreTunnelID,'hpnicfNvgreTunnelRowStatus':hpnicfNvgreTunnelRowStatus,'hpnicfNvgreTunnelOctets':hpnicfNvgreTunnelOctets,'hpnicfNvgreTunnelPackets':hpnicfNvgreTunnelPackets,'hpnicfNvgreTunnelBoundTable':hpnicfNvgreTunnelBoundTable,'hpnicfNvgreTunnelBoundEntry':hpnicfNvgreTunnelBoundEntry,'hpnicfNvgreTunnelBoundNvgreNum':hpnicfNvgreTunnelBoundNvgreNum,'hpnicfNvgreMacTable':hpnicfNvgreMacTable,'hpnicfNvgreMacEntry':hpnicfNvgreMacEntry,_J:hpnicfNvgreMacAddr,'hpnicfNvgreMacTunnelID':hpnicfNvgreMacTunnelID,'hpnicfNvgreMacType':hpnicfNvgreMacType,'hpnicfNvgreStaticMacTable':hpnicfNvgreStaticMacTable,'hpnicfNvgreStaticMacEntry':hpnicfNvgreStaticMacEntry,_K:hpnicfNvgreStaticMacAddr,'hpnicfNvgreStaticMacTunnelID':hpnicfNvgreStaticMacTunnelID,'hpnicfNvgreStaticMacRowStatus':hpnicfNvgreStaticMacRowStatus})