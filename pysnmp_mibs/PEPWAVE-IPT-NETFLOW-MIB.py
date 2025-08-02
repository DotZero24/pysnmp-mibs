_AO='iptNetflowSockGroup'
_AN='iptNetflowCpuGroup'
_AM='iptNetflowTotalsGroup'
_AL='iptNetflowSysctlGroup'
_AK='iptNetflowModuleGroup'
_AJ='sockSndbufPeak'
_AI='sockSndbufFill'
_AH='sockSndbuf'
_AG='sockErrOther'
_AF='sockErrCberr'
_AE='sockErrFull'
_AD='sockErrConnect'
_AC='sockActive'
_AB='sockDestination'
_AA='cpuErrMaxflows'
_A9='cpuErrAlloc'
_A8='cpuErrFrag'
_A7='cpuErrTrunc'
_A6='cpuDropBytes'
_A5='cpuDropPackets'
_A4='cpuHashMetric'
_A3='cpuInBytes'
_A2='cpuInPackets'
_A1='cpuInFlows'
_A0='cpuInPacketRate'
_z='sndbufPeak'
_y='errTotal'
_x='lostBytes'
_w='lostPackets'
_v='lostFlows'
_u='outBytes'
_t='outPackets'
_s='outFlows'
_r='outByteRate'
_q='dropBytes'
_p='dropPackets'
_o='hashBytes'
_n='hashPackets'
_m='hashFlows'
_l='hashMemory'
_k='hashMetric'
_j='inBytes'
_i='inPackets'
_h='inFlows'
_g='inPacketRate'
_f='inBitRate'
_e='scan-min'
_d='snmp-rules'
_c='promisc'
_b='natevents'
_a='sampler'
_Z='aggregation'
_Y='destination'
_X='sndbuf'
_W='inactive-timeout'
_V='active-timeout'
_U='protocol'
_T='maxflows'
_S='hashsize'
_R='refcnt'
_Q='loadTime'
_P='srcversion'
_O='version'
_N='sockIndex'
_M='packets/second'
_L='enabled'
_K='disabled'
_J='minutes'
_I='cpuIndex'
_H='flows'
_G='packets'
_F='Integer32'
_E='bytes'
_D='read-write'
_C='read-only'
_B='PEPWAVE-IPT-NETFLOW-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
iptNetflowMIB=ModuleIdentity((1,3,6,1,4,1,27662,200,1,15))
class FixedDiv100(TextualConvention,Gauge32):status=_A;displayHint='d-2'
_Pepwave_ObjectIdentity=ObjectIdentity
pepwave=_Pepwave_ObjectIdentity((1,3,6,1,4,1,27662))
_ProductMib_ObjectIdentity=ObjectIdentity
productMib=_ProductMib_ObjectIdentity((1,3,6,1,4,1,27662,200))
_GeneralMib_ObjectIdentity=ObjectIdentity
generalMib=_GeneralMib_ObjectIdentity((1,3,6,1,4,1,27662,200,1))
_IptNetflowObjects_ObjectIdentity=ObjectIdentity
iptNetflowObjects=_IptNetflowObjects_ObjectIdentity((1,3,6,1,4,1,27662,200,1,15,1))
_IptNetflowModule_ObjectIdentity=ObjectIdentity
iptNetflowModule=_IptNetflowModule_ObjectIdentity((1,3,6,1,4,1,27662,200,1,15,1,1))
_Name_Type=DisplayString
_Name_Object=MibScalar
name=_Name_Object((1,3,6,1,4,1,27662,200,1,15,1,1,1),_Name_Type())
name.setMaxAccess(_C)
if mibBuilder.loadTexts:name.setStatus(_A)
_Version_Type=DisplayString
_Version_Object=MibScalar
version=_Version_Object((1,3,6,1,4,1,27662,200,1,15,1,1,2),_Version_Type())
version.setMaxAccess(_C)
if mibBuilder.loadTexts:version.setStatus(_A)
_Srcversion_Type=DisplayString
_Srcversion_Object=MibScalar
srcversion=_Srcversion_Object((1,3,6,1,4,1,27662,200,1,15,1,1,3),_Srcversion_Type())
srcversion.setMaxAccess(_C)
if mibBuilder.loadTexts:srcversion.setStatus(_A)
_LoadTime_Type=DateAndTime
_LoadTime_Object=MibScalar
loadTime=_LoadTime_Object((1,3,6,1,4,1,27662,200,1,15,1,1,4),_LoadTime_Type())
loadTime.setMaxAccess(_C)
if mibBuilder.loadTexts:loadTime.setStatus(_A)
_Refcnt_Type=Integer32
_Refcnt_Object=MibScalar
refcnt=_Refcnt_Object((1,3,6,1,4,1,27662,200,1,15,1,1,5),_Refcnt_Type())
refcnt.setMaxAccess(_C)
if mibBuilder.loadTexts:refcnt.setStatus(_A)
_IptNetflowSysctl_ObjectIdentity=ObjectIdentity
iptNetflowSysctl=_IptNetflowSysctl_ObjectIdentity((1,3,6,1,4,1,27662,200,1,15,1,2))
class _Protocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,9,10)));namedValues=NamedValues(*(('netflow5',5),('netflow9',9),('ipfix',10)))
_Protocol_Type.__name__=_F
_Protocol_Object=MibScalar
protocol=_Protocol_Object((1,3,6,1,4,1,27662,200,1,15,1,2,1),_Protocol_Type())
protocol.setMaxAccess(_D)
if mibBuilder.loadTexts:protocol.setStatus(_A)
_Hashsize_Type=Integer32
_Hashsize_Object=MibScalar
hashsize=_Hashsize_Object((1,3,6,1,4,1,27662,200,1,15,1,2,2),_Hashsize_Type())
hashsize.setMaxAccess(_D)
if mibBuilder.loadTexts:hashsize.setStatus(_A)
if mibBuilder.loadTexts:hashsize.setUnits('buckets')
_Maxflows_Type=Integer32
_Maxflows_Object=MibScalar
maxflows=_Maxflows_Object((1,3,6,1,4,1,27662,200,1,15,1,2,3),_Maxflows_Type())
maxflows.setMaxAccess(_D)
if mibBuilder.loadTexts:maxflows.setStatus(_A)
if mibBuilder.loadTexts:maxflows.setUnits(_H)
_Active_timeout_Type=Integer32
_Active_timeout_Object=MibScalar
active_timeout=_Active_timeout_Object((1,3,6,1,4,1,27662,200,1,15,1,2,4),_Active_timeout_Type())
active_timeout.setMaxAccess(_D)
if mibBuilder.loadTexts:active_timeout.setStatus(_A)
if mibBuilder.loadTexts:active_timeout.setUnits(_J)
_Inactive_timeout_Type=Integer32
_Inactive_timeout_Object=MibScalar
inactive_timeout=_Inactive_timeout_Object((1,3,6,1,4,1,27662,200,1,15,1,2,5),_Inactive_timeout_Type())
inactive_timeout.setMaxAccess(_D)
if mibBuilder.loadTexts:inactive_timeout.setStatus(_A)
if mibBuilder.loadTexts:inactive_timeout.setUnits(_J)
_Sndbuf_Type=Integer32
_Sndbuf_Object=MibScalar
sndbuf=_Sndbuf_Object((1,3,6,1,4,1,27662,200,1,15,1,2,6),_Sndbuf_Type())
sndbuf.setMaxAccess(_D)
if mibBuilder.loadTexts:sndbuf.setStatus(_A)
if mibBuilder.loadTexts:sndbuf.setUnits(_E)
_Destination_Type=DisplayString
_Destination_Object=MibScalar
destination=_Destination_Object((1,3,6,1,4,1,27662,200,1,15,1,2,7),_Destination_Type())
destination.setMaxAccess(_D)
if mibBuilder.loadTexts:destination.setStatus(_A)
_Aggregation_Type=DisplayString
_Aggregation_Object=MibScalar
aggregation=_Aggregation_Object((1,3,6,1,4,1,27662,200,1,15,1,2,8),_Aggregation_Type())
aggregation.setMaxAccess(_D)
if mibBuilder.loadTexts:aggregation.setStatus(_A)
_Sampler_Type=DisplayString
_Sampler_Object=MibScalar
sampler=_Sampler_Object((1,3,6,1,4,1,27662,200,1,15,1,2,9),_Sampler_Type())
sampler.setMaxAccess(_D)
if mibBuilder.loadTexts:sampler.setStatus(_A)
class _Natevents_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_Natevents_Type.__name__=_F
_Natevents_Object=MibScalar
natevents=_Natevents_Object((1,3,6,1,4,1,27662,200,1,15,1,2,10),_Natevents_Type())
natevents.setMaxAccess(_D)
if mibBuilder.loadTexts:natevents.setStatus(_A)
class _Promisc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_Promisc_Type.__name__=_F
_Promisc_Object=MibScalar
promisc=_Promisc_Object((1,3,6,1,4,1,27662,200,1,15,1,2,11),_Promisc_Type())
promisc.setMaxAccess(_D)
if mibBuilder.loadTexts:promisc.setStatus(_A)
_Snmp_rules_Type=DisplayString
_Snmp_rules_Object=MibScalar
snmp_rules=_Snmp_rules_Object((1,3,6,1,4,1,27662,200,1,15,1,2,12),_Snmp_rules_Type())
snmp_rules.setMaxAccess(_D)
if mibBuilder.loadTexts:snmp_rules.setStatus(_A)
_Scan_min_Type=Integer32
_Scan_min_Object=MibScalar
scan_min=_Scan_min_Object((1,3,6,1,4,1,27662,200,1,15,1,2,13),_Scan_min_Type())
scan_min.setMaxAccess(_D)
if mibBuilder.loadTexts:scan_min.setStatus(_A)
_IptNetflowStatistics_ObjectIdentity=ObjectIdentity
iptNetflowStatistics=_IptNetflowStatistics_ObjectIdentity((1,3,6,1,4,1,27662,200,1,15,2))
_IptNetflowTotals_ObjectIdentity=ObjectIdentity
iptNetflowTotals=_IptNetflowTotals_ObjectIdentity((1,3,6,1,4,1,27662,200,1,15,2,1))
_InBitRate_Type=CounterBasedGauge64
_InBitRate_Object=MibScalar
inBitRate=_InBitRate_Object((1,3,6,1,4,1,27662,200,1,15,2,1,1),_InBitRate_Type())
inBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:inBitRate.setStatus(_A)
if mibBuilder.loadTexts:inBitRate.setUnits('bits/second')
_InPacketRate_Type=Gauge32
_InPacketRate_Object=MibScalar
inPacketRate=_InPacketRate_Object((1,3,6,1,4,1,27662,200,1,15,2,1,2),_InPacketRate_Type())
inPacketRate.setMaxAccess(_C)
if mibBuilder.loadTexts:inPacketRate.setStatus(_A)
if mibBuilder.loadTexts:inPacketRate.setUnits(_M)
_InFlows_Type=Counter64
_InFlows_Object=MibScalar
inFlows=_InFlows_Object((1,3,6,1,4,1,27662,200,1,15,2,1,3),_InFlows_Type())
inFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:inFlows.setStatus(_A)
if mibBuilder.loadTexts:inFlows.setUnits(_H)
_InPackets_Type=Counter64
_InPackets_Object=MibScalar
inPackets=_InPackets_Object((1,3,6,1,4,1,27662,200,1,15,2,1,4),_InPackets_Type())
inPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:inPackets.setStatus(_A)
if mibBuilder.loadTexts:inPackets.setUnits(_G)
_InBytes_Type=Counter64
_InBytes_Object=MibScalar
inBytes=_InBytes_Object((1,3,6,1,4,1,27662,200,1,15,2,1,5),_InBytes_Type())
inBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:inBytes.setStatus(_A)
if mibBuilder.loadTexts:inBytes.setUnits(_E)
_HashMetric_Type=FixedDiv100
_HashMetric_Object=MibScalar
hashMetric=_HashMetric_Object((1,3,6,1,4,1,27662,200,1,15,2,1,6),_HashMetric_Type())
hashMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:hashMetric.setStatus(_A)
_HashMemory_Type=Gauge32
_HashMemory_Object=MibScalar
hashMemory=_HashMemory_Object((1,3,6,1,4,1,27662,200,1,15,2,1,7),_HashMemory_Type())
hashMemory.setMaxAccess(_C)
if mibBuilder.loadTexts:hashMemory.setStatus(_A)
if mibBuilder.loadTexts:hashMemory.setUnits(_E)
_HashFlows_Type=Gauge32
_HashFlows_Object=MibScalar
hashFlows=_HashFlows_Object((1,3,6,1,4,1,27662,200,1,15,2,1,8),_HashFlows_Type())
hashFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:hashFlows.setStatus(_A)
if mibBuilder.loadTexts:hashFlows.setUnits(_H)
_HashPackets_Type=Gauge32
_HashPackets_Object=MibScalar
hashPackets=_HashPackets_Object((1,3,6,1,4,1,27662,200,1,15,2,1,9),_HashPackets_Type())
hashPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hashPackets.setStatus(_A)
if mibBuilder.loadTexts:hashPackets.setUnits(_G)
_HashBytes_Type=CounterBasedGauge64
_HashBytes_Object=MibScalar
hashBytes=_HashBytes_Object((1,3,6,1,4,1,27662,200,1,15,2,1,10),_HashBytes_Type())
hashBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hashBytes.setStatus(_A)
if mibBuilder.loadTexts:hashBytes.setUnits(_E)
_DropPackets_Type=Counter64
_DropPackets_Object=MibScalar
dropPackets=_DropPackets_Object((1,3,6,1,4,1,27662,200,1,15,2,1,11),_DropPackets_Type())
dropPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:dropPackets.setStatus(_A)
if mibBuilder.loadTexts:dropPackets.setUnits(_G)
_DropBytes_Type=Counter64
_DropBytes_Object=MibScalar
dropBytes=_DropBytes_Object((1,3,6,1,4,1,27662,200,1,15,2,1,12),_DropBytes_Type())
dropBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:dropBytes.setStatus(_A)
if mibBuilder.loadTexts:dropBytes.setUnits(_E)
_OutByteRate_Type=Gauge32
_OutByteRate_Object=MibScalar
outByteRate=_OutByteRate_Object((1,3,6,1,4,1,27662,200,1,15,2,1,13),_OutByteRate_Type())
outByteRate.setMaxAccess(_C)
if mibBuilder.loadTexts:outByteRate.setStatus(_A)
if mibBuilder.loadTexts:outByteRate.setUnits('bytes/second')
_OutFlows_Type=Counter64
_OutFlows_Object=MibScalar
outFlows=_OutFlows_Object((1,3,6,1,4,1,27662,200,1,15,2,1,14),_OutFlows_Type())
outFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:outFlows.setStatus(_A)
if mibBuilder.loadTexts:outFlows.setUnits(_H)
_OutPackets_Type=Counter64
_OutPackets_Object=MibScalar
outPackets=_OutPackets_Object((1,3,6,1,4,1,27662,200,1,15,2,1,15),_OutPackets_Type())
outPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:outPackets.setStatus(_A)
if mibBuilder.loadTexts:outPackets.setUnits(_G)
_OutBytes_Type=Counter64
_OutBytes_Object=MibScalar
outBytes=_OutBytes_Object((1,3,6,1,4,1,27662,200,1,15,2,1,16),_OutBytes_Type())
outBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:outBytes.setStatus(_A)
if mibBuilder.loadTexts:outBytes.setUnits(_E)
_LostFlows_Type=Counter64
_LostFlows_Object=MibScalar
lostFlows=_LostFlows_Object((1,3,6,1,4,1,27662,200,1,15,2,1,17),_LostFlows_Type())
lostFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:lostFlows.setStatus(_A)
if mibBuilder.loadTexts:lostFlows.setUnits(_H)
_LostPackets_Type=Counter64
_LostPackets_Object=MibScalar
lostPackets=_LostPackets_Object((1,3,6,1,4,1,27662,200,1,15,2,1,18),_LostPackets_Type())
lostPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:lostPackets.setStatus(_A)
if mibBuilder.loadTexts:lostPackets.setUnits(_G)
_LostBytes_Type=Counter64
_LostBytes_Object=MibScalar
lostBytes=_LostBytes_Object((1,3,6,1,4,1,27662,200,1,15,2,1,19),_LostBytes_Type())
lostBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:lostBytes.setStatus(_A)
if mibBuilder.loadTexts:lostBytes.setUnits(_E)
_ErrTotal_Type=Counter32
_ErrTotal_Object=MibScalar
errTotal=_ErrTotal_Object((1,3,6,1,4,1,27662,200,1,15,2,1,20),_ErrTotal_Type())
errTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:errTotal.setStatus(_A)
_SndbufPeak_Type=Counter32
_SndbufPeak_Object=MibScalar
sndbufPeak=_SndbufPeak_Object((1,3,6,1,4,1,27662,200,1,15,2,1,21),_SndbufPeak_Type())
sndbufPeak.setMaxAccess(_C)
if mibBuilder.loadTexts:sndbufPeak.setStatus(_A)
if mibBuilder.loadTexts:sndbufPeak.setUnits(_E)
_IptNetflowCpuTable_Object=MibTable
iptNetflowCpuTable=_IptNetflowCpuTable_Object((1,3,6,1,4,1,27662,200,1,15,2,2))
if mibBuilder.loadTexts:iptNetflowCpuTable.setStatus(_A)
_IptNetflowCpuEntry_Object=MibTableRow
iptNetflowCpuEntry=_IptNetflowCpuEntry_Object((1,3,6,1,4,1,27662,200,1,15,2,2,1))
iptNetflowCpuEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:iptNetflowCpuEntry.setStatus(_A)
class _CpuIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_CpuIndex_Type.__name__=_F
_CpuIndex_Object=MibTableColumn
cpuIndex=_CpuIndex_Object((1,3,6,1,4,1,27662,200,1,15,2,2,1,1),_CpuIndex_Type())
cpuIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuIndex.setStatus(_A)
_CpuInPacketRate_Type=Gauge32
_CpuInPacketRate_Object=MibTableColumn
cpuInPacketRate=_CpuInPacketRate_Object((1,3,6,1,4,1,27662,200,1,15,2,2,1,2),_CpuInPacketRate_Type())
cpuInPacketRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuInPacketRate.setStatus(_A)
if mibBuilder.loadTexts:cpuInPacketRate.setUnits(_M)
_CpuInFlows_Type=Counter64
_CpuInFlows_Object=MibTableColumn
cpuInFlows=_CpuInFlows_Object((1,3,6,1,4,1,27662,200,1,15,2,2,1,3),_CpuInFlows_Type())
cpuInFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuInFlows.setStatus(_A)
if mibBuilder.loadTexts:cpuInFlows.setUnits(_H)
_CpuInPackets_Type=Counter64
_CpuInPackets_Object=MibTableColumn
cpuInPackets=_CpuInPackets_Object((1,3,6,1,4,1,27662,200,1,15,2,2,1,4),_CpuInPackets_Type())
cpuInPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuInPackets.setStatus(_A)
if mibBuilder.loadTexts:cpuInPackets.setUnits(_G)
_CpuInBytes_Type=Counter64
_CpuInBytes_Object=MibTableColumn
cpuInBytes=_CpuInBytes_Object((1,3,6,1,4,1,27662,200,1,15,2,2,1,5),_CpuInBytes_Type())
cpuInBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuInBytes.setStatus(_A)
if mibBuilder.loadTexts:cpuInBytes.setUnits(_E)
_CpuHashMetric_Type=FixedDiv100
_CpuHashMetric_Object=MibTableColumn
cpuHashMetric=_CpuHashMetric_Object((1,3,6,1,4,1,27662,200,1,15,2,2,1,6),_CpuHashMetric_Type())
cpuHashMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuHashMetric.setStatus(_A)
_CpuDropPackets_Type=Counter64
_CpuDropPackets_Object=MibTableColumn
cpuDropPackets=_CpuDropPackets_Object((1,3,6,1,4,1,27662,200,1,15,2,2,1,7),_CpuDropPackets_Type())
cpuDropPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuDropPackets.setStatus(_A)
if mibBuilder.loadTexts:cpuDropPackets.setUnits(_G)
_CpuDropBytes_Type=Counter64
_CpuDropBytes_Object=MibTableColumn
cpuDropBytes=_CpuDropBytes_Object((1,3,6,1,4,1,27662,200,1,15,2,2,1,8),_CpuDropBytes_Type())
cpuDropBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuDropBytes.setStatus(_A)
if mibBuilder.loadTexts:cpuDropBytes.setUnits(_E)
_CpuErrTrunc_Type=Counter32
_CpuErrTrunc_Object=MibTableColumn
cpuErrTrunc=_CpuErrTrunc_Object((1,3,6,1,4,1,27662,200,1,15,2,2,1,9),_CpuErrTrunc_Type())
cpuErrTrunc.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuErrTrunc.setStatus(_A)
_CpuErrFrag_Type=Counter32
_CpuErrFrag_Object=MibTableColumn
cpuErrFrag=_CpuErrFrag_Object((1,3,6,1,4,1,27662,200,1,15,2,2,1,10),_CpuErrFrag_Type())
cpuErrFrag.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuErrFrag.setStatus(_A)
_CpuErrAlloc_Type=Counter32
_CpuErrAlloc_Object=MibTableColumn
cpuErrAlloc=_CpuErrAlloc_Object((1,3,6,1,4,1,27662,200,1,15,2,2,1,11),_CpuErrAlloc_Type())
cpuErrAlloc.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuErrAlloc.setStatus(_A)
_CpuErrMaxflows_Type=Counter32
_CpuErrMaxflows_Object=MibTableColumn
cpuErrMaxflows=_CpuErrMaxflows_Object((1,3,6,1,4,1,27662,200,1,15,2,2,1,12),_CpuErrMaxflows_Type())
cpuErrMaxflows.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuErrMaxflows.setStatus(_A)
_IptNetflowSockTable_Object=MibTable
iptNetflowSockTable=_IptNetflowSockTable_Object((1,3,6,1,4,1,27662,200,1,15,2,3))
if mibBuilder.loadTexts:iptNetflowSockTable.setStatus(_A)
_IptNetflowSockEntry_Object=MibTableRow
iptNetflowSockEntry=_IptNetflowSockEntry_Object((1,3,6,1,4,1,27662,200,1,15,2,3,1))
iptNetflowSockEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:iptNetflowSockEntry.setStatus(_A)
class _SockIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_SockIndex_Type.__name__=_F
_SockIndex_Object=MibTableColumn
sockIndex=_SockIndex_Object((1,3,6,1,4,1,27662,200,1,15,2,3,1,1),_SockIndex_Type())
sockIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:sockIndex.setStatus(_A)
_SockDestination_Type=DisplayString
_SockDestination_Object=MibTableColumn
sockDestination=_SockDestination_Object((1,3,6,1,4,1,27662,200,1,15,2,3,1,2),_SockDestination_Type())
sockDestination.setMaxAccess(_C)
if mibBuilder.loadTexts:sockDestination.setStatus(_A)
class _SockActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('inactive',0),('active',1)))
_SockActive_Type.__name__=_F
_SockActive_Object=MibTableColumn
sockActive=_SockActive_Object((1,3,6,1,4,1,27662,200,1,15,2,3,1,3),_SockActive_Type())
sockActive.setMaxAccess(_C)
if mibBuilder.loadTexts:sockActive.setStatus(_A)
_SockErrConnect_Type=Counter32
_SockErrConnect_Object=MibTableColumn
sockErrConnect=_SockErrConnect_Object((1,3,6,1,4,1,27662,200,1,15,2,3,1,4),_SockErrConnect_Type())
sockErrConnect.setMaxAccess(_C)
if mibBuilder.loadTexts:sockErrConnect.setStatus(_A)
_SockErrFull_Type=Counter32
_SockErrFull_Object=MibTableColumn
sockErrFull=_SockErrFull_Object((1,3,6,1,4,1,27662,200,1,15,2,3,1,5),_SockErrFull_Type())
sockErrFull.setMaxAccess(_C)
if mibBuilder.loadTexts:sockErrFull.setStatus(_A)
_SockErrCberr_Type=Counter32
_SockErrCberr_Object=MibTableColumn
sockErrCberr=_SockErrCberr_Object((1,3,6,1,4,1,27662,200,1,15,2,3,1,6),_SockErrCberr_Type())
sockErrCberr.setMaxAccess(_C)
if mibBuilder.loadTexts:sockErrCberr.setStatus(_A)
_SockErrOther_Type=Counter32
_SockErrOther_Object=MibTableColumn
sockErrOther=_SockErrOther_Object((1,3,6,1,4,1,27662,200,1,15,2,3,1,7),_SockErrOther_Type())
sockErrOther.setMaxAccess(_C)
if mibBuilder.loadTexts:sockErrOther.setStatus(_A)
_SockSndbuf_Type=Gauge32
_SockSndbuf_Object=MibTableColumn
sockSndbuf=_SockSndbuf_Object((1,3,6,1,4,1,27662,200,1,15,2,3,1,8),_SockSndbuf_Type())
sockSndbuf.setMaxAccess(_C)
if mibBuilder.loadTexts:sockSndbuf.setStatus(_A)
if mibBuilder.loadTexts:sockSndbuf.setUnits(_E)
_SockSndbufFill_Type=Gauge32
_SockSndbufFill_Object=MibTableColumn
sockSndbufFill=_SockSndbufFill_Object((1,3,6,1,4,1,27662,200,1,15,2,3,1,9),_SockSndbufFill_Type())
sockSndbufFill.setMaxAccess(_C)
if mibBuilder.loadTexts:sockSndbufFill.setStatus(_A)
if mibBuilder.loadTexts:sockSndbufFill.setUnits(_E)
_SockSndbufPeak_Type=Gauge32
_SockSndbufPeak_Object=MibTableColumn
sockSndbufPeak=_SockSndbufPeak_Object((1,3,6,1,4,1,27662,200,1,15,2,3,1,10),_SockSndbufPeak_Type())
sockSndbufPeak.setMaxAccess(_C)
if mibBuilder.loadTexts:sockSndbufPeak.setStatus(_A)
if mibBuilder.loadTexts:sockSndbufPeak.setUnits(_E)
_IptNetflowConformance_ObjectIdentity=ObjectIdentity
iptNetflowConformance=_IptNetflowConformance_ObjectIdentity((1,3,6,1,4,1,27662,200,1,15,3))
_IptNetflowCompliances_ObjectIdentity=ObjectIdentity
iptNetflowCompliances=_IptNetflowCompliances_ObjectIdentity((1,3,6,1,4,1,27662,200,1,15,3,1))
_IptNetflowGroups_ObjectIdentity=ObjectIdentity
iptNetflowGroups=_IptNetflowGroups_ObjectIdentity((1,3,6,1,4,1,27662,200,1,15,3,2))
iptNetflowModuleGroup=ObjectGroup((1,3,6,1,4,1,27662,200,1,15,3,2,1))
iptNetflowModuleGroup.setObjects(*((_B,'name'),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:iptNetflowModuleGroup.setStatus(_A)
iptNetflowSysctlGroup=ObjectGroup((1,3,6,1,4,1,27662,200,1,15,3,2,2))
iptNetflowSysctlGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:iptNetflowSysctlGroup.setStatus(_A)
iptNetflowTotalsGroup=ObjectGroup((1,3,6,1,4,1,27662,200,1,15,3,2,3))
iptNetflowTotalsGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:iptNetflowTotalsGroup.setStatus(_A)
iptNetflowCpuGroup=ObjectGroup((1,3,6,1,4,1,27662,200,1,15,3,2,4))
iptNetflowCpuGroup.setObjects(*((_B,_I),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:iptNetflowCpuGroup.setStatus(_A)
iptNetflowSockGroup=ObjectGroup((1,3,6,1,4,1,27662,200,1,15,3,2,5))
iptNetflowSockGroup.setObjects(*((_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:iptNetflowSockGroup.setStatus(_A)
iptNetflowCompliance=ModuleCompliance((1,3,6,1,4,1,27662,200,1,15,3,1,1))
iptNetflowCompliance.setObjects(*((_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO)))
if mibBuilder.loadTexts:iptNetflowCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'FixedDiv100':FixedDiv100,'pepwave':pepwave,'productMib':productMib,'generalMib':generalMib,'iptNetflowMIB':iptNetflowMIB,'iptNetflowObjects':iptNetflowObjects,'iptNetflowModule':iptNetflowModule,'name':name,_O:version,_P:srcversion,_Q:loadTime,_R:refcnt,'iptNetflowSysctl':iptNetflowSysctl,_U:protocol,_S:hashsize,_T:maxflows,_V:active_timeout,_W:inactive_timeout,_X:sndbuf,_Y:destination,_Z:aggregation,_a:sampler,_b:natevents,_c:promisc,_d:snmp_rules,_e:scan_min,'iptNetflowStatistics':iptNetflowStatistics,'iptNetflowTotals':iptNetflowTotals,_f:inBitRate,_g:inPacketRate,_h:inFlows,_i:inPackets,_j:inBytes,_k:hashMetric,_l:hashMemory,_m:hashFlows,_n:hashPackets,_o:hashBytes,_p:dropPackets,_q:dropBytes,_r:outByteRate,_s:outFlows,_t:outPackets,_u:outBytes,_v:lostFlows,_w:lostPackets,_x:lostBytes,_y:errTotal,_z:sndbufPeak,'iptNetflowCpuTable':iptNetflowCpuTable,'iptNetflowCpuEntry':iptNetflowCpuEntry,_I:cpuIndex,_A0:cpuInPacketRate,_A1:cpuInFlows,_A2:cpuInPackets,_A3:cpuInBytes,_A4:cpuHashMetric,_A5:cpuDropPackets,_A6:cpuDropBytes,_A7:cpuErrTrunc,_A8:cpuErrFrag,_A9:cpuErrAlloc,_AA:cpuErrMaxflows,'iptNetflowSockTable':iptNetflowSockTable,'iptNetflowSockEntry':iptNetflowSockEntry,_N:sockIndex,_AB:sockDestination,_AC:sockActive,_AD:sockErrConnect,_AE:sockErrFull,_AF:sockErrCberr,_AG:sockErrOther,_AH:sockSndbuf,_AI:sockSndbufFill,_AJ:sockSndbufPeak,'iptNetflowConformance':iptNetflowConformance,'iptNetflowCompliances':iptNetflowCompliances,'iptNetflowCompliance':iptNetflowCompliance,'iptNetflowGroups':iptNetflowGroups,_AK:iptNetflowModuleGroup,_AL:iptNetflowSysctlGroup,_AM:iptNetflowTotalsGroup,_AN:iptNetflowCpuGroup,_AO:iptNetflowSockGroup})