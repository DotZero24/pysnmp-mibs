_E='collectorIndex'
_D='TPT-SFLOW-MIB'
_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tpt_tpa_objs,=mibBuilder.importSymbols('TPT-TPAMIBS-MIB','tpt-tpa-objs')
tpt_sflow_objs=ModuleIdentity((1,3,6,1,4,1,10734,3,3,2,18))
if mibBuilder.loadTexts:tpt_sflow_objs.setRevisions(('2016-05-25 18:54',))
class SflowStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('disable',0),('enable',1),('error',2),('not-applicable',3)))
_SFlowCollectorTable_Object=MibTable
sFlowCollectorTable=_SFlowCollectorTable_Object((1,3,6,1,4,1,10734,3,3,2,18,1))
if mibBuilder.loadTexts:sFlowCollectorTable.setStatus(_A)
_SFlowCollectorEntry_Object=MibTableRow
sFlowCollectorEntry=_SFlowCollectorEntry_Object((1,3,6,1,4,1,10734,3,3,2,18,1,1))
sFlowCollectorEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:sFlowCollectorEntry.setStatus(_A)
_CollectorIndex_Type=Unsigned32
_CollectorIndex_Object=MibTableColumn
collectorIndex=_CollectorIndex_Object((1,3,6,1,4,1,10734,3,3,2,18,1,1,1),_CollectorIndex_Type())
collectorIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:collectorIndex.setStatus(_A)
class _CollectorAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CollectorAddr_Type.__name__=_C
_CollectorAddr_Object=MibTableColumn
collectorAddr=_CollectorAddr_Object((1,3,6,1,4,1,10734,3,3,2,18,1,1,2),_CollectorAddr_Type())
collectorAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:collectorAddr.setStatus(_A)
_UdpPort_Type=Unsigned32
_UdpPort_Object=MibTableColumn
udpPort=_UdpPort_Object((1,3,6,1,4,1,10734,3,3,2,18,1,1,3),_UdpPort_Type())
udpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:udpPort.setStatus(_A)
class _CollectorAddrV6_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,60))
_CollectorAddrV6_Type.__name__=_C
_CollectorAddrV6_Object=MibTableColumn
collectorAddrV6=_CollectorAddrV6_Object((1,3,6,1,4,1,10734,3,3,2,18,1,1,4),_CollectorAddrV6_Type())
collectorAddrV6.setMaxAccess(_B)
if mibBuilder.loadTexts:collectorAddrV6.setStatus(_A)
_SFlowStatus_Type=SflowStatus
_SFlowStatus_Object=MibScalar
sFlowStatus=_SFlowStatus_Object((1,3,6,1,4,1,10734,3,3,2,18,2),_SFlowStatus_Type())
sFlowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sFlowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'SflowStatus':SflowStatus,'tpt-sflow-objs':tpt_sflow_objs,'sFlowCollectorTable':sFlowCollectorTable,'sFlowCollectorEntry':sFlowCollectorEntry,_E:collectorIndex,'collectorAddr':collectorAddr,'udpPort':udpPort,'collectorAddrV6':collectorAddrV6,'sFlowStatus':sFlowStatus})