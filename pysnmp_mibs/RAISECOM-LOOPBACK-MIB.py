_L='rcL3LoopbackPortNum'
_K='rcL2LoopbackPortNum'
_J='read-only'
_I='enable'
_H='disable'
_G='not-accessible'
_F='rcLoopbackPortIndex'
_E='read-write'
_D='RAISECOM-LOOPBACK-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
rcLoopback=ModuleIdentity((1,3,6,1,4,1,8886,6,1,73))
if mibBuilder.loadTexts:rcLoopback.setRevisions(('2012-08-02 00:00',))
_RcLoopbackPortTable_Object=MibTable
rcLoopbackPortTable=_RcLoopbackPortTable_Object((1,3,6,1,4,1,8886,6,1,73,1))
if mibBuilder.loadTexts:rcLoopbackPortTable.setStatus(_A)
_RcLoopbackPortEntry_Object=MibTableRow
rcLoopbackPortEntry=_RcLoopbackPortEntry_Object((1,3,6,1,4,1,8886,6,1,73,1,1))
rcLoopbackPortEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:rcLoopbackPortEntry.setStatus(_A)
_RcLoopbackPortIndex_Type=Integer32
_RcLoopbackPortIndex_Object=MibTableColumn
rcLoopbackPortIndex=_RcLoopbackPortIndex_Object((1,3,6,1,4,1,8886,6,1,73,1,1,1),_RcLoopbackPortIndex_Type())
rcLoopbackPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rcLoopbackPortIndex.setStatus(_A)
class _RcLoopbackPortEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_RcLoopbackPortEnable_Type.__name__=_C
_RcLoopbackPortEnable_Object=MibTableColumn
rcLoopbackPortEnable=_RcLoopbackPortEnable_Object((1,3,6,1,4,1,8886,6,1,73,1,1,2),_RcLoopbackPortEnable_Type())
rcLoopbackPortEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rcLoopbackPortEnable.setStatus(_A)
class _RcLoopbackPortMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('l1',1),('l2',2),('l3',3)))
_RcLoopbackPortMode_Type.__name__=_C
_RcLoopbackPortMode_Object=MibTableColumn
rcLoopbackPortMode=_RcLoopbackPortMode_Object((1,3,6,1,4,1,8886,6,1,73,1,1,3),_RcLoopbackPortMode_Type())
rcLoopbackPortMode.setMaxAccess(_E)
if mibBuilder.loadTexts:rcLoopbackPortMode.setStatus(_A)
_RcLoopbackPortStatistics_Type=Counter32
_RcLoopbackPortStatistics_Object=MibTableColumn
rcLoopbackPortStatistics=_RcLoopbackPortStatistics_Object((1,3,6,1,4,1,8886,6,1,73,1,1,4),_RcLoopbackPortStatistics_Type())
rcLoopbackPortStatistics.setMaxAccess(_J)
if mibBuilder.loadTexts:rcLoopbackPortStatistics.setStatus(_A)
class _RcLoopbackPortClearStatistics_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_RcLoopbackPortClearStatistics_Type.__name__=_C
_RcLoopbackPortClearStatistics_Object=MibTableColumn
rcLoopbackPortClearStatistics=_RcLoopbackPortClearStatistics_Object((1,3,6,1,4,1,8886,6,1,73,1,1,5),_RcLoopbackPortClearStatistics_Type())
rcLoopbackPortClearStatistics.setMaxAccess(_E)
if mibBuilder.loadTexts:rcLoopbackPortClearStatistics.setStatus(_A)
_RcLoopbackPortSmac_Type=MacAddress
_RcLoopbackPortSmac_Object=MibTableColumn
rcLoopbackPortSmac=_RcLoopbackPortSmac_Object((1,3,6,1,4,1,8886,6,1,73,1,1,6),_RcLoopbackPortSmac_Type())
rcLoopbackPortSmac.setMaxAccess(_E)
if mibBuilder.loadTexts:rcLoopbackPortSmac.setStatus(_A)
_RcLoopbackPortProtocol_Type=Integer32
_RcLoopbackPortProtocol_Object=MibTableColumn
rcLoopbackPortProtocol=_RcLoopbackPortProtocol_Object((1,3,6,1,4,1,8886,6,1,73,1,1,7),_RcLoopbackPortProtocol_Type())
rcLoopbackPortProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:rcLoopbackPortProtocol.setStatus(_A)
class _RcLoopbackPortVlan_Type(Integer32):defaultValue=1
_RcLoopbackPortVlan_Type.__name__=_C
_RcLoopbackPortVlan_Object=MibTableColumn
rcLoopbackPortVlan=_RcLoopbackPortVlan_Object((1,3,6,1,4,1,8886,6,1,73,1,1,8),_RcLoopbackPortVlan_Type())
rcLoopbackPortVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:rcLoopbackPortVlan.setStatus(_A)
_RcL2LoopbackPortTable_Object=MibTable
rcL2LoopbackPortTable=_RcL2LoopbackPortTable_Object((1,3,6,1,4,1,8886,6,1,73,2))
if mibBuilder.loadTexts:rcL2LoopbackPortTable.setStatus(_A)
_RcL2LoopbackPortEntry_Object=MibTableRow
rcL2LoopbackPortEntry=_RcL2LoopbackPortEntry_Object((1,3,6,1,4,1,8886,6,1,73,2,1))
rcL2LoopbackPortEntry.setIndexNames((0,_D,_F),(0,_D,_K))
if mibBuilder.loadTexts:rcL2LoopbackPortEntry.setStatus(_A)
_RcL2LoopbackPortNum_Type=Integer32
_RcL2LoopbackPortNum_Object=MibTableColumn
rcL2LoopbackPortNum=_RcL2LoopbackPortNum_Object((1,3,6,1,4,1,8886,6,1,73,2,1,1),_RcL2LoopbackPortNum_Type())
rcL2LoopbackPortNum.setMaxAccess(_G)
if mibBuilder.loadTexts:rcL2LoopbackPortNum.setStatus(_A)
_RcL2LoopbackPortStatistics_Type=Counter32
_RcL2LoopbackPortStatistics_Object=MibTableColumn
rcL2LoopbackPortStatistics=_RcL2LoopbackPortStatistics_Object((1,3,6,1,4,1,8886,6,1,73,2,1,2),_RcL2LoopbackPortStatistics_Type())
rcL2LoopbackPortStatistics.setMaxAccess(_J)
if mibBuilder.loadTexts:rcL2LoopbackPortStatistics.setStatus(_A)
_RcL2LoopbackPortSmac_Type=MacAddress
_RcL2LoopbackPortSmac_Object=MibTableColumn
rcL2LoopbackPortSmac=_RcL2LoopbackPortSmac_Object((1,3,6,1,4,1,8886,6,1,73,2,1,3),_RcL2LoopbackPortSmac_Type())
rcL2LoopbackPortSmac.setMaxAccess(_B)
if mibBuilder.loadTexts:rcL2LoopbackPortSmac.setStatus(_A)
_RcL2LoopbackPortProtocol_Type=Integer32
_RcL2LoopbackPortProtocol_Object=MibTableColumn
rcL2LoopbackPortProtocol=_RcL2LoopbackPortProtocol_Object((1,3,6,1,4,1,8886,6,1,73,2,1,4),_RcL2LoopbackPortProtocol_Type())
rcL2LoopbackPortProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:rcL2LoopbackPortProtocol.setStatus(_A)
class _RcL2LoopbackPortVlan_Type(Integer32):defaultValue=1
_RcL2LoopbackPortVlan_Type.__name__=_C
_RcL2LoopbackPortVlan_Object=MibTableColumn
rcL2LoopbackPortVlan=_RcL2LoopbackPortVlan_Object((1,3,6,1,4,1,8886,6,1,73,2,1,5),_RcL2LoopbackPortVlan_Type())
rcL2LoopbackPortVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:rcL2LoopbackPortVlan.setStatus(_A)
_RcL2LoopbackPortStatus_Type=RowStatus
_RcL2LoopbackPortStatus_Object=MibTableColumn
rcL2LoopbackPortStatus=_RcL2LoopbackPortStatus_Object((1,3,6,1,4,1,8886,6,1,73,2,1,6),_RcL2LoopbackPortStatus_Type())
rcL2LoopbackPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcL2LoopbackPortStatus.setStatus(_A)
_RcL3LoopbackPortTable_Object=MibTable
rcL3LoopbackPortTable=_RcL3LoopbackPortTable_Object((1,3,6,1,4,1,8886,6,1,73,3))
if mibBuilder.loadTexts:rcL3LoopbackPortTable.setStatus(_A)
_RcL3LoopbackPortEntry_Object=MibTableRow
rcL3LoopbackPortEntry=_RcL3LoopbackPortEntry_Object((1,3,6,1,4,1,8886,6,1,73,3,1))
rcL3LoopbackPortEntry.setIndexNames((0,_D,_F),(0,_D,_L))
if mibBuilder.loadTexts:rcL3LoopbackPortEntry.setStatus(_A)
_RcL3LoopbackPortNum_Type=Integer32
_RcL3LoopbackPortNum_Object=MibTableColumn
rcL3LoopbackPortNum=_RcL3LoopbackPortNum_Object((1,3,6,1,4,1,8886,6,1,73,3,1,1),_RcL3LoopbackPortNum_Type())
rcL3LoopbackPortNum.setMaxAccess(_G)
if mibBuilder.loadTexts:rcL3LoopbackPortNum.setStatus(_A)
_RcL3LoopbackPortDestAddr_Type=IpAddress
_RcL3LoopbackPortDestAddr_Object=MibTableColumn
rcL3LoopbackPortDestAddr=_RcL3LoopbackPortDestAddr_Object((1,3,6,1,4,1,8886,6,1,73,3,1,2),_RcL3LoopbackPortDestAddr_Type())
rcL3LoopbackPortDestAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rcL3LoopbackPortDestAddr.setStatus(_A)
_RcL3LoopbackPortMAC_Type=MacAddress
_RcL3LoopbackPortMAC_Object=MibTableColumn
rcL3LoopbackPortMAC=_RcL3LoopbackPortMAC_Object((1,3,6,1,4,1,8886,6,1,73,3,1,3),_RcL3LoopbackPortMAC_Type())
rcL3LoopbackPortMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:rcL3LoopbackPortMAC.setStatus(_A)
class _RcL3LoopbackPortSvlan_Type(Integer32):defaultValue=1
_RcL3LoopbackPortSvlan_Type.__name__=_C
_RcL3LoopbackPortSvlan_Object=MibTableColumn
rcL3LoopbackPortSvlan=_RcL3LoopbackPortSvlan_Object((1,3,6,1,4,1,8886,6,1,73,3,1,4),_RcL3LoopbackPortSvlan_Type())
rcL3LoopbackPortSvlan.setMaxAccess(_B)
if mibBuilder.loadTexts:rcL3LoopbackPortSvlan.setStatus(_A)
class _RcL3LoopbackPortCvlan_Type(Integer32):defaultValue=1
_RcL3LoopbackPortCvlan_Type.__name__=_C
_RcL3LoopbackPortCvlan_Object=MibTableColumn
rcL3LoopbackPortCvlan=_RcL3LoopbackPortCvlan_Object((1,3,6,1,4,1,8886,6,1,73,3,1,5),_RcL3LoopbackPortCvlan_Type())
rcL3LoopbackPortCvlan.setMaxAccess(_B)
if mibBuilder.loadTexts:rcL3LoopbackPortCvlan.setStatus(_A)
class _RcL3LoopbackPortDscp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RcL3LoopbackPortDscp_Type.__name__=_C
_RcL3LoopbackPortDscp_Object=MibTableColumn
rcL3LoopbackPortDscp=_RcL3LoopbackPortDscp_Object((1,3,6,1,4,1,8886,6,1,73,3,1,6),_RcL3LoopbackPortDscp_Type())
rcL3LoopbackPortDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:rcL3LoopbackPortDscp.setStatus(_A)
_RcL3LoopbackPortStatus_Type=RowStatus
_RcL3LoopbackPortStatus_Object=MibTableColumn
rcL3LoopbackPortStatus=_RcL3LoopbackPortStatus_Object((1,3,6,1,4,1,8886,6,1,73,3,1,7),_RcL3LoopbackPortStatus_Type())
rcL3LoopbackPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcL3LoopbackPortStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'rcLoopback':rcLoopback,'rcLoopbackPortTable':rcLoopbackPortTable,'rcLoopbackPortEntry':rcLoopbackPortEntry,_F:rcLoopbackPortIndex,'rcLoopbackPortEnable':rcLoopbackPortEnable,'rcLoopbackPortMode':rcLoopbackPortMode,'rcLoopbackPortStatistics':rcLoopbackPortStatistics,'rcLoopbackPortClearStatistics':rcLoopbackPortClearStatistics,'rcLoopbackPortSmac':rcLoopbackPortSmac,'rcLoopbackPortProtocol':rcLoopbackPortProtocol,'rcLoopbackPortVlan':rcLoopbackPortVlan,'rcL2LoopbackPortTable':rcL2LoopbackPortTable,'rcL2LoopbackPortEntry':rcL2LoopbackPortEntry,_K:rcL2LoopbackPortNum,'rcL2LoopbackPortStatistics':rcL2LoopbackPortStatistics,'rcL2LoopbackPortSmac':rcL2LoopbackPortSmac,'rcL2LoopbackPortProtocol':rcL2LoopbackPortProtocol,'rcL2LoopbackPortVlan':rcL2LoopbackPortVlan,'rcL2LoopbackPortStatus':rcL2LoopbackPortStatus,'rcL3LoopbackPortTable':rcL3LoopbackPortTable,'rcL3LoopbackPortEntry':rcL3LoopbackPortEntry,_L:rcL3LoopbackPortNum,'rcL3LoopbackPortDestAddr':rcL3LoopbackPortDestAddr,'rcL3LoopbackPortMAC':rcL3LoopbackPortMAC,'rcL3LoopbackPortSvlan':rcL3LoopbackPortSvlan,'rcL3LoopbackPortCvlan':rcL3LoopbackPortCvlan,'rcL3LoopbackPortDscp':rcL3LoopbackPortDscp,'rcL3LoopbackPortStatus':rcL3LoopbackPortStatus})