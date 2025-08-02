_K='h3cNvgreStaticMacAddr'
_J='h3cNvgreMacAddr'
_I='Integer32'
_H='h3cNvgreVsiIndex'
_G='h3cNvgreTunnelID'
_F='h3cNvgreID'
_E='not-accessible'
_D='read-create'
_C='read-only'
_B='H3C-NVGRE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
h3cNvgre=ModuleIdentity((1,3,6,1,4,1,2011,10,2,156))
if mibBuilder.loadTexts:h3cNvgre.setRevisions(('2014-03-11 09:00',))
_H3cNvgreObjects_ObjectIdentity=ObjectIdentity
h3cNvgreObjects=_H3cNvgreObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,156,1))
_H3cNvgreScalarGroup_ObjectIdentity=ObjectIdentity
h3cNvgreScalarGroup=_H3cNvgreScalarGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,156,1,1))
_H3cNvgreNextNvgreID_Type=Unsigned32
_H3cNvgreNextNvgreID_Object=MibScalar
h3cNvgreNextNvgreID=_H3cNvgreNextNvgreID_Object((1,3,6,1,4,1,2011,10,2,156,1,1,1),_H3cNvgreNextNvgreID_Type())
h3cNvgreNextNvgreID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNvgreNextNvgreID.setStatus(_A)
_H3cNvgreConfigured_Type=Unsigned32
_H3cNvgreConfigured_Object=MibScalar
h3cNvgreConfigured=_H3cNvgreConfigured_Object((1,3,6,1,4,1,2011,10,2,156,1,1,2),_H3cNvgreConfigured_Type())
h3cNvgreConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNvgreConfigured.setStatus(_A)
_H3cNvgreTable_Object=MibTable
h3cNvgreTable=_H3cNvgreTable_Object((1,3,6,1,4,1,2011,10,2,156,1,2))
if mibBuilder.loadTexts:h3cNvgreTable.setStatus(_A)
_H3cNvgreEntry_Object=MibTableRow
h3cNvgreEntry=_H3cNvgreEntry_Object((1,3,6,1,4,1,2011,10,2,156,1,2,1))
h3cNvgreEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:h3cNvgreEntry.setStatus(_A)
_H3cNvgreID_Type=Unsigned32
_H3cNvgreID_Object=MibTableColumn
h3cNvgreID=_H3cNvgreID_Object((1,3,6,1,4,1,2011,10,2,156,1,2,1,1),_H3cNvgreID_Type())
h3cNvgreID.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cNvgreID.setStatus(_A)
_H3cNvgreVsiIndex_Type=Unsigned32
_H3cNvgreVsiIndex_Object=MibTableColumn
h3cNvgreVsiIndex=_H3cNvgreVsiIndex_Object((1,3,6,1,4,1,2011,10,2,156,1,2,1,2),_H3cNvgreVsiIndex_Type())
h3cNvgreVsiIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cNvgreVsiIndex.setStatus(_A)
_H3cNvgreRemoteMacCount_Type=Unsigned32
_H3cNvgreRemoteMacCount_Object=MibTableColumn
h3cNvgreRemoteMacCount=_H3cNvgreRemoteMacCount_Object((1,3,6,1,4,1,2011,10,2,156,1,2,1,3),_H3cNvgreRemoteMacCount_Type())
h3cNvgreRemoteMacCount.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNvgreRemoteMacCount.setStatus(_A)
_H3cNvgreRowStatus_Type=RowStatus
_H3cNvgreRowStatus_Object=MibTableColumn
h3cNvgreRowStatus=_H3cNvgreRowStatus_Object((1,3,6,1,4,1,2011,10,2,156,1,2,1,4),_H3cNvgreRowStatus_Type())
h3cNvgreRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cNvgreRowStatus.setStatus(_A)
_H3cNvgreTunnelTable_Object=MibTable
h3cNvgreTunnelTable=_H3cNvgreTunnelTable_Object((1,3,6,1,4,1,2011,10,2,156,1,3))
if mibBuilder.loadTexts:h3cNvgreTunnelTable.setStatus(_A)
_H3cNvgreTunnelEntry_Object=MibTableRow
h3cNvgreTunnelEntry=_H3cNvgreTunnelEntry_Object((1,3,6,1,4,1,2011,10,2,156,1,3,1))
h3cNvgreTunnelEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:h3cNvgreTunnelEntry.setStatus(_A)
_H3cNvgreTunnelID_Type=Unsigned32
_H3cNvgreTunnelID_Object=MibTableColumn
h3cNvgreTunnelID=_H3cNvgreTunnelID_Object((1,3,6,1,4,1,2011,10,2,156,1,3,1,1),_H3cNvgreTunnelID_Type())
h3cNvgreTunnelID.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cNvgreTunnelID.setStatus(_A)
_H3cNvgreTunnelRowStatus_Type=RowStatus
_H3cNvgreTunnelRowStatus_Object=MibTableColumn
h3cNvgreTunnelRowStatus=_H3cNvgreTunnelRowStatus_Object((1,3,6,1,4,1,2011,10,2,156,1,3,1,2),_H3cNvgreTunnelRowStatus_Type())
h3cNvgreTunnelRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cNvgreTunnelRowStatus.setStatus(_A)
_H3cNvgreTunnelOctets_Type=Counter64
_H3cNvgreTunnelOctets_Object=MibTableColumn
h3cNvgreTunnelOctets=_H3cNvgreTunnelOctets_Object((1,3,6,1,4,1,2011,10,2,156,1,3,1,3),_H3cNvgreTunnelOctets_Type())
h3cNvgreTunnelOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNvgreTunnelOctets.setStatus(_A)
_H3cNvgreTunnelPackets_Type=Counter64
_H3cNvgreTunnelPackets_Object=MibTableColumn
h3cNvgreTunnelPackets=_H3cNvgreTunnelPackets_Object((1,3,6,1,4,1,2011,10,2,156,1,3,1,4),_H3cNvgreTunnelPackets_Type())
h3cNvgreTunnelPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNvgreTunnelPackets.setStatus(_A)
_H3cNvgreTunnelBoundTable_Object=MibTable
h3cNvgreTunnelBoundTable=_H3cNvgreTunnelBoundTable_Object((1,3,6,1,4,1,2011,10,2,156,1,4))
if mibBuilder.loadTexts:h3cNvgreTunnelBoundTable.setStatus(_A)
_H3cNvgreTunnelBoundEntry_Object=MibTableRow
h3cNvgreTunnelBoundEntry=_H3cNvgreTunnelBoundEntry_Object((1,3,6,1,4,1,2011,10,2,156,1,4,1))
h3cNvgreTunnelBoundEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:h3cNvgreTunnelBoundEntry.setStatus(_A)
_H3cNvgreTunnelBoundNvgreNum_Type=Unsigned32
_H3cNvgreTunnelBoundNvgreNum_Object=MibTableColumn
h3cNvgreTunnelBoundNvgreNum=_H3cNvgreTunnelBoundNvgreNum_Object((1,3,6,1,4,1,2011,10,2,156,1,4,1,1),_H3cNvgreTunnelBoundNvgreNum_Type())
h3cNvgreTunnelBoundNvgreNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNvgreTunnelBoundNvgreNum.setStatus(_A)
_H3cNvgreMacTable_Object=MibTable
h3cNvgreMacTable=_H3cNvgreMacTable_Object((1,3,6,1,4,1,2011,10,2,156,1,5))
if mibBuilder.loadTexts:h3cNvgreMacTable.setStatus(_A)
_H3cNvgreMacEntry_Object=MibTableRow
h3cNvgreMacEntry=_H3cNvgreMacEntry_Object((1,3,6,1,4,1,2011,10,2,156,1,5,1))
h3cNvgreMacEntry.setIndexNames((0,_B,_H),(0,_B,_J))
if mibBuilder.loadTexts:h3cNvgreMacEntry.setStatus(_A)
_H3cNvgreMacAddr_Type=MacAddress
_H3cNvgreMacAddr_Object=MibTableColumn
h3cNvgreMacAddr=_H3cNvgreMacAddr_Object((1,3,6,1,4,1,2011,10,2,156,1,5,1,1),_H3cNvgreMacAddr_Type())
h3cNvgreMacAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cNvgreMacAddr.setStatus(_A)
_H3cNvgreMacTunnelID_Type=Unsigned32
_H3cNvgreMacTunnelID_Object=MibTableColumn
h3cNvgreMacTunnelID=_H3cNvgreMacTunnelID_Object((1,3,6,1,4,1,2011,10,2,156,1,5,1,2),_H3cNvgreMacTunnelID_Type())
h3cNvgreMacTunnelID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNvgreMacTunnelID.setStatus(_A)
class _H3cNvgreMacType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('selfLearned',1),('staticConfigured',2),('protocolLearned',3)))
_H3cNvgreMacType_Type.__name__=_I
_H3cNvgreMacType_Object=MibTableColumn
h3cNvgreMacType=_H3cNvgreMacType_Object((1,3,6,1,4,1,2011,10,2,156,1,5,1,3),_H3cNvgreMacType_Type())
h3cNvgreMacType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNvgreMacType.setStatus(_A)
_H3cNvgreStaticMacTable_Object=MibTable
h3cNvgreStaticMacTable=_H3cNvgreStaticMacTable_Object((1,3,6,1,4,1,2011,10,2,156,1,6))
if mibBuilder.loadTexts:h3cNvgreStaticMacTable.setStatus(_A)
_H3cNvgreStaticMacEntry_Object=MibTableRow
h3cNvgreStaticMacEntry=_H3cNvgreStaticMacEntry_Object((1,3,6,1,4,1,2011,10,2,156,1,6,1))
h3cNvgreStaticMacEntry.setIndexNames((0,_B,_H),(0,_B,_K))
if mibBuilder.loadTexts:h3cNvgreStaticMacEntry.setStatus(_A)
_H3cNvgreStaticMacAddr_Type=MacAddress
_H3cNvgreStaticMacAddr_Object=MibTableColumn
h3cNvgreStaticMacAddr=_H3cNvgreStaticMacAddr_Object((1,3,6,1,4,1,2011,10,2,156,1,6,1,1),_H3cNvgreStaticMacAddr_Type())
h3cNvgreStaticMacAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cNvgreStaticMacAddr.setStatus(_A)
_H3cNvgreStaticMacTunnelID_Type=Unsigned32
_H3cNvgreStaticMacTunnelID_Object=MibTableColumn
h3cNvgreStaticMacTunnelID=_H3cNvgreStaticMacTunnelID_Object((1,3,6,1,4,1,2011,10,2,156,1,6,1,2),_H3cNvgreStaticMacTunnelID_Type())
h3cNvgreStaticMacTunnelID.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cNvgreStaticMacTunnelID.setStatus(_A)
_H3cNvgreStaticMacRowStatus_Type=RowStatus
_H3cNvgreStaticMacRowStatus_Object=MibTableColumn
h3cNvgreStaticMacRowStatus=_H3cNvgreStaticMacRowStatus_Object((1,3,6,1,4,1,2011,10,2,156,1,6,1,3),_H3cNvgreStaticMacRowStatus_Type())
h3cNvgreStaticMacRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cNvgreStaticMacRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cNvgre':h3cNvgre,'h3cNvgreObjects':h3cNvgreObjects,'h3cNvgreScalarGroup':h3cNvgreScalarGroup,'h3cNvgreNextNvgreID':h3cNvgreNextNvgreID,'h3cNvgreConfigured':h3cNvgreConfigured,'h3cNvgreTable':h3cNvgreTable,'h3cNvgreEntry':h3cNvgreEntry,_F:h3cNvgreID,_H:h3cNvgreVsiIndex,'h3cNvgreRemoteMacCount':h3cNvgreRemoteMacCount,'h3cNvgreRowStatus':h3cNvgreRowStatus,'h3cNvgreTunnelTable':h3cNvgreTunnelTable,'h3cNvgreTunnelEntry':h3cNvgreTunnelEntry,_G:h3cNvgreTunnelID,'h3cNvgreTunnelRowStatus':h3cNvgreTunnelRowStatus,'h3cNvgreTunnelOctets':h3cNvgreTunnelOctets,'h3cNvgreTunnelPackets':h3cNvgreTunnelPackets,'h3cNvgreTunnelBoundTable':h3cNvgreTunnelBoundTable,'h3cNvgreTunnelBoundEntry':h3cNvgreTunnelBoundEntry,'h3cNvgreTunnelBoundNvgreNum':h3cNvgreTunnelBoundNvgreNum,'h3cNvgreMacTable':h3cNvgreMacTable,'h3cNvgreMacEntry':h3cNvgreMacEntry,_J:h3cNvgreMacAddr,'h3cNvgreMacTunnelID':h3cNvgreMacTunnelID,'h3cNvgreMacType':h3cNvgreMacType,'h3cNvgreStaticMacTable':h3cNvgreStaticMacTable,'h3cNvgreStaticMacEntry':h3cNvgreStaticMacEntry,_K:h3cNvgreStaticMacAddr,'h3cNvgreStaticMacTunnelID':h3cNvgreStaticMacTunnelID,'h3cNvgreStaticMacRowStatus':h3cNvgreStaticMacRowStatus})