_F='ifCnCpuIndex'
_E='ifCnIndex'
_D='CAMBIUM-NETWORKS-INTERF-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
cnInterfaces=ModuleIdentity((1,3,6,1,4,1,17713,24,11))
if mibBuilder.loadTexts:cnInterfaces.setRevisions(('2022-05-26 00:00','2021-11-30 00:00','2021-04-08 18:00'))
_IfCnTablePortLinkTransitions_Object=MibTable
ifCnTablePortLinkTransitions=_IfCnTablePortLinkTransitions_Object((1,3,6,1,4,1,17713,24,11,1))
if mibBuilder.loadTexts:ifCnTablePortLinkTransitions.setStatus(_A)
_IfCnEntry_Object=MibTableRow
ifCnEntry=_IfCnEntry_Object((1,3,6,1,4,1,17713,24,11,1,1))
ifCnEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ifCnEntry.setStatus(_A)
class _IfCnIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IfCnIndex_Type.__name__=_C
_IfCnIndex_Object=MibTableColumn
ifCnIndex=_IfCnIndex_Object((1,3,6,1,4,1,17713,24,11,1,1,1),_IfCnIndex_Type())
ifCnIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ifCnIndex.setStatus(_A)
_IfCnPortLinkTransitions_Type=Gauge32
_IfCnPortLinkTransitions_Object=MibTableColumn
ifCnPortLinkTransitions=_IfCnPortLinkTransitions_Object((1,3,6,1,4,1,17713,24,11,1,1,2),_IfCnPortLinkTransitions_Type())
ifCnPortLinkTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:ifCnPortLinkTransitions.setStatus(_A)
_IfCnPortCpuStatisticsTable_Object=MibTable
ifCnPortCpuStatisticsTable=_IfCnPortCpuStatisticsTable_Object((1,3,6,1,4,1,17713,24,11,2))
if mibBuilder.loadTexts:ifCnPortCpuStatisticsTable.setStatus(_A)
_IfCnCpuEntry_Object=MibTableRow
ifCnCpuEntry=_IfCnCpuEntry_Object((1,3,6,1,4,1,17713,24,11,2,1))
ifCnCpuEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:ifCnCpuEntry.setStatus(_A)
class _IfCnCpuIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IfCnCpuIndex_Type.__name__=_C
_IfCnCpuIndex_Object=MibTableColumn
ifCnCpuIndex=_IfCnCpuIndex_Object((1,3,6,1,4,1,17713,24,11,2,1,1),_IfCnCpuIndex_Type())
ifCnCpuIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ifCnCpuIndex.setStatus(_A)
_IfCnCpuRxUcastPkts_Type=Counter32
_IfCnCpuRxUcastPkts_Object=MibTableColumn
ifCnCpuRxUcastPkts=_IfCnCpuRxUcastPkts_Object((1,3,6,1,4,1,17713,24,11,2,1,2),_IfCnCpuRxUcastPkts_Type())
ifCnCpuRxUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifCnCpuRxUcastPkts.setStatus(_A)
_IfCnCpuRxMcastPkts_Type=Counter32
_IfCnCpuRxMcastPkts_Object=MibTableColumn
ifCnCpuRxMcastPkts=_IfCnCpuRxMcastPkts_Object((1,3,6,1,4,1,17713,24,11,2,1,3),_IfCnCpuRxMcastPkts_Type())
ifCnCpuRxMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifCnCpuRxMcastPkts.setStatus(_A)
_IfCnCpuRxBcastPkts_Type=Counter32
_IfCnCpuRxBcastPkts_Object=MibTableColumn
ifCnCpuRxBcastPkts=_IfCnCpuRxBcastPkts_Object((1,3,6,1,4,1,17713,24,11,2,1,4),_IfCnCpuRxBcastPkts_Type())
ifCnCpuRxBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifCnCpuRxBcastPkts.setStatus(_A)
_IfCnCpuRxArpPkts_Type=Counter32
_IfCnCpuRxArpPkts_Object=MibTableColumn
ifCnCpuRxArpPkts=_IfCnCpuRxArpPkts_Object((1,3,6,1,4,1,17713,24,11,2,1,5),_IfCnCpuRxArpPkts_Type())
ifCnCpuRxArpPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifCnCpuRxArpPkts.setStatus(_A)
_IfCnCpuRxIgmpPkts_Type=Counter32
_IfCnCpuRxIgmpPkts_Object=MibTableColumn
ifCnCpuRxIgmpPkts=_IfCnCpuRxIgmpPkts_Object((1,3,6,1,4,1,17713,24,11,2,1,6),_IfCnCpuRxIgmpPkts_Type())
ifCnCpuRxIgmpPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifCnCpuRxIgmpPkts.setStatus(_A)
_IfCnCpuRxIpMcastPkts_Type=Counter32
_IfCnCpuRxIpMcastPkts_Object=MibTableColumn
ifCnCpuRxIpMcastPkts=_IfCnCpuRxIpMcastPkts_Object((1,3,6,1,4,1,17713,24,11,2,1,7),_IfCnCpuRxIpMcastPkts_Type())
ifCnCpuRxIpMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifCnCpuRxIpMcastPkts.setStatus(_A)
_IfCnCpuRxStpPkts_Type=Counter32
_IfCnCpuRxStpPkts_Object=MibTableColumn
ifCnCpuRxStpPkts=_IfCnCpuRxStpPkts_Object((1,3,6,1,4,1,17713,24,11,2,1,8),_IfCnCpuRxStpPkts_Type())
ifCnCpuRxStpPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifCnCpuRxStpPkts.setStatus(_A)
_IfCnCpuRxLldpPkts_Type=Counter32
_IfCnCpuRxLldpPkts_Object=MibTableColumn
ifCnCpuRxLldpPkts=_IfCnCpuRxLldpPkts_Object((1,3,6,1,4,1,17713,24,11,2,1,9),_IfCnCpuRxLldpPkts_Type())
ifCnCpuRxLldpPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifCnCpuRxLldpPkts.setStatus(_A)
_IfCnCpuRxDhcpPkts_Type=Counter32
_IfCnCpuRxDhcpPkts_Object=MibTableColumn
ifCnCpuRxDhcpPkts=_IfCnCpuRxDhcpPkts_Object((1,3,6,1,4,1,17713,24,11,2,1,10),_IfCnCpuRxDhcpPkts_Type())
ifCnCpuRxDhcpPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifCnCpuRxDhcpPkts.setStatus(_A)
_IfCnCpuRxOtherPkts_Type=Counter32
_IfCnCpuRxOtherPkts_Object=MibTableColumn
ifCnCpuRxOtherPkts=_IfCnCpuRxOtherPkts_Object((1,3,6,1,4,1,17713,24,11,2,1,11),_IfCnCpuRxOtherPkts_Type())
ifCnCpuRxOtherPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifCnCpuRxOtherPkts.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'cnInterfaces':cnInterfaces,'ifCnTablePortLinkTransitions':ifCnTablePortLinkTransitions,'ifCnEntry':ifCnEntry,_E:ifCnIndex,'ifCnPortLinkTransitions':ifCnPortLinkTransitions,'ifCnPortCpuStatisticsTable':ifCnPortCpuStatisticsTable,'ifCnCpuEntry':ifCnCpuEntry,_F:ifCnCpuIndex,'ifCnCpuRxUcastPkts':ifCnCpuRxUcastPkts,'ifCnCpuRxMcastPkts':ifCnCpuRxMcastPkts,'ifCnCpuRxBcastPkts':ifCnCpuRxBcastPkts,'ifCnCpuRxArpPkts':ifCnCpuRxArpPkts,'ifCnCpuRxIgmpPkts':ifCnCpuRxIgmpPkts,'ifCnCpuRxIpMcastPkts':ifCnCpuRxIpMcastPkts,'ifCnCpuRxStpPkts':ifCnCpuRxStpPkts,'ifCnCpuRxLldpPkts':ifCnCpuRxLldpPkts,'ifCnCpuRxDhcpPkts':ifCnCpuRxDhcpPkts,'ifCnCpuRxOtherPkts':ifCnCpuRxOtherPkts})