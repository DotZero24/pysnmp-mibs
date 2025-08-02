_J='zhoneIpEntry'
_I='not-accessible'
_H='zhIpNetToMediaNetAddress'
_G='zhIpNetToMediaIfIndex'
_F='read-write'
_E='read-create'
_D='ZHONE-COM-IP-IP-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rdEntry,=mibBuilder.importSymbols('ZHONE-COM-IP-RD-MIB','rdEntry')
zhoneIp,zhoneModules=mibBuilder.importSymbols('Zhone','zhoneIp','zhoneModules')
ZhoneRowStatus,=mibBuilder.importSymbols('Zhone-TC','ZhoneRowStatus')
comIpIp=ModuleIdentity((1,3,6,1,4,1,5504,6,54))
if mibBuilder.loadTexts:comIpIp.setRevisions(('2000-11-02 17:30','2000-09-11 16:30'))
_Ip_ObjectIdentity=ObjectIdentity
ip=_Ip_ObjectIdentity((1,3,6,1,4,1,5504,4,1,4))
if mibBuilder.loadTexts:ip.setStatus(_A)
_ZhoneIpTable_Object=MibTable
zhoneIpTable=_ZhoneIpTable_Object((1,3,6,1,4,1,5504,4,1,4,2))
if mibBuilder.loadTexts:zhoneIpTable.setStatus(_A)
_ZhoneIpEntry_Object=MibTableRow
zhoneIpEntry=_ZhoneIpEntry_Object((1,3,6,1,4,1,5504,4,1,4,2,1))
if mibBuilder.loadTexts:zhoneIpEntry.setStatus(_A)
class _ZhIpForwarding_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forwarding',1),('notForwarding',2)))
_ZhIpForwarding_Type.__name__=_C
_ZhIpForwarding_Object=MibTableColumn
zhIpForwarding=_ZhIpForwarding_Object((1,3,6,1,4,1,5504,4,1,4,2,1,1),_ZhIpForwarding_Type())
zhIpForwarding.setMaxAccess(_F)
if mibBuilder.loadTexts:zhIpForwarding.setStatus(_A)
class _ZhIpDefaultTTL_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ZhIpDefaultTTL_Type.__name__=_C
_ZhIpDefaultTTL_Object=MibTableColumn
zhIpDefaultTTL=_ZhIpDefaultTTL_Object((1,3,6,1,4,1,5504,4,1,4,2,1,2),_ZhIpDefaultTTL_Type())
zhIpDefaultTTL.setMaxAccess(_F)
if mibBuilder.loadTexts:zhIpDefaultTTL.setStatus(_A)
_ZhIpInReceives_Type=Counter32
_ZhIpInReceives_Object=MibTableColumn
zhIpInReceives=_ZhIpInReceives_Object((1,3,6,1,4,1,5504,4,1,4,2,1,3),_ZhIpInReceives_Type())
zhIpInReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIpInReceives.setStatus(_A)
_ZhIpInHdrErrors_Type=Counter32
_ZhIpInHdrErrors_Object=MibTableColumn
zhIpInHdrErrors=_ZhIpInHdrErrors_Object((1,3,6,1,4,1,5504,4,1,4,2,1,4),_ZhIpInHdrErrors_Type())
zhIpInHdrErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIpInHdrErrors.setStatus(_A)
_ZhIpInAddrErrors_Type=Counter32
_ZhIpInAddrErrors_Object=MibTableColumn
zhIpInAddrErrors=_ZhIpInAddrErrors_Object((1,3,6,1,4,1,5504,4,1,4,2,1,5),_ZhIpInAddrErrors_Type())
zhIpInAddrErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIpInAddrErrors.setStatus(_A)
_ZhIpForwDatagrams_Type=Counter32
_ZhIpForwDatagrams_Object=MibTableColumn
zhIpForwDatagrams=_ZhIpForwDatagrams_Object((1,3,6,1,4,1,5504,4,1,4,2,1,6),_ZhIpForwDatagrams_Type())
zhIpForwDatagrams.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIpForwDatagrams.setStatus(_A)
_ZhIpInUnknownProtos_Type=Counter32
_ZhIpInUnknownProtos_Object=MibTableColumn
zhIpInUnknownProtos=_ZhIpInUnknownProtos_Object((1,3,6,1,4,1,5504,4,1,4,2,1,7),_ZhIpInUnknownProtos_Type())
zhIpInUnknownProtos.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIpInUnknownProtos.setStatus(_A)
_ZhIpInDiscards_Type=Counter32
_ZhIpInDiscards_Object=MibTableColumn
zhIpInDiscards=_ZhIpInDiscards_Object((1,3,6,1,4,1,5504,4,1,4,2,1,8),_ZhIpInDiscards_Type())
zhIpInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIpInDiscards.setStatus(_A)
_ZhIpInDelivers_Type=Counter32
_ZhIpInDelivers_Object=MibTableColumn
zhIpInDelivers=_ZhIpInDelivers_Object((1,3,6,1,4,1,5504,4,1,4,2,1,9),_ZhIpInDelivers_Type())
zhIpInDelivers.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIpInDelivers.setStatus(_A)
_ZhIpOutRequests_Type=Counter32
_ZhIpOutRequests_Object=MibTableColumn
zhIpOutRequests=_ZhIpOutRequests_Object((1,3,6,1,4,1,5504,4,1,4,2,1,10),_ZhIpOutRequests_Type())
zhIpOutRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIpOutRequests.setStatus(_A)
_ZhIpOutDiscards_Type=Counter32
_ZhIpOutDiscards_Object=MibTableColumn
zhIpOutDiscards=_ZhIpOutDiscards_Object((1,3,6,1,4,1,5504,4,1,4,2,1,11),_ZhIpOutDiscards_Type())
zhIpOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIpOutDiscards.setStatus(_A)
_ZhIpOutNoRoutes_Type=Counter32
_ZhIpOutNoRoutes_Object=MibTableColumn
zhIpOutNoRoutes=_ZhIpOutNoRoutes_Object((1,3,6,1,4,1,5504,4,1,4,2,1,12),_ZhIpOutNoRoutes_Type())
zhIpOutNoRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIpOutNoRoutes.setStatus(_A)
_ZhIpReasmTimeout_Type=Unsigned32
_ZhIpReasmTimeout_Object=MibTableColumn
zhIpReasmTimeout=_ZhIpReasmTimeout_Object((1,3,6,1,4,1,5504,4,1,4,2,1,13),_ZhIpReasmTimeout_Type())
zhIpReasmTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIpReasmTimeout.setStatus(_A)
if mibBuilder.loadTexts:zhIpReasmTimeout.setUnits('seconds')
_ZhIpReasmReqds_Type=Counter32
_ZhIpReasmReqds_Object=MibTableColumn
zhIpReasmReqds=_ZhIpReasmReqds_Object((1,3,6,1,4,1,5504,4,1,4,2,1,14),_ZhIpReasmReqds_Type())
zhIpReasmReqds.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIpReasmReqds.setStatus(_A)
_ZhIpReasmOKs_Type=Counter32
_ZhIpReasmOKs_Object=MibTableColumn
zhIpReasmOKs=_ZhIpReasmOKs_Object((1,3,6,1,4,1,5504,4,1,4,2,1,15),_ZhIpReasmOKs_Type())
zhIpReasmOKs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIpReasmOKs.setStatus(_A)
_ZhIpReasmFails_Type=Counter32
_ZhIpReasmFails_Object=MibTableColumn
zhIpReasmFails=_ZhIpReasmFails_Object((1,3,6,1,4,1,5504,4,1,4,2,1,16),_ZhIpReasmFails_Type())
zhIpReasmFails.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIpReasmFails.setStatus(_A)
_ZhIpFragOKs_Type=Counter32
_ZhIpFragOKs_Object=MibTableColumn
zhIpFragOKs=_ZhIpFragOKs_Object((1,3,6,1,4,1,5504,4,1,4,2,1,17),_ZhIpFragOKs_Type())
zhIpFragOKs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIpFragOKs.setStatus(_A)
_ZhIpFragFails_Type=Counter32
_ZhIpFragFails_Object=MibTableColumn
zhIpFragFails=_ZhIpFragFails_Object((1,3,6,1,4,1,5504,4,1,4,2,1,18),_ZhIpFragFails_Type())
zhIpFragFails.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIpFragFails.setStatus(_A)
_ZhIpFragCreates_Type=Counter32
_ZhIpFragCreates_Object=MibTableColumn
zhIpFragCreates=_ZhIpFragCreates_Object((1,3,6,1,4,1,5504,4,1,4,2,1,19),_ZhIpFragCreates_Type())
zhIpFragCreates.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIpFragCreates.setStatus(_A)
_ZhIpRoutingDiscards_Type=Counter32
_ZhIpRoutingDiscards_Object=MibTableColumn
zhIpRoutingDiscards=_ZhIpRoutingDiscards_Object((1,3,6,1,4,1,5504,4,1,4,2,1,20),_ZhIpRoutingDiscards_Type())
zhIpRoutingDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIpRoutingDiscards.setStatus(_A)
_ZhoneIpNetToMediaTable_Object=MibTable
zhoneIpNetToMediaTable=_ZhoneIpNetToMediaTable_Object((1,3,6,1,4,1,5504,4,1,4,4))
if mibBuilder.loadTexts:zhoneIpNetToMediaTable.setStatus(_A)
_ZhoneIpNetToMediaEntry_Object=MibTableRow
zhoneIpNetToMediaEntry=_ZhoneIpNetToMediaEntry_Object((1,3,6,1,4,1,5504,4,1,4,4,1))
zhoneIpNetToMediaEntry.setIndexNames((0,_D,_G),(0,_D,_H))
if mibBuilder.loadTexts:zhoneIpNetToMediaEntry.setStatus(_A)
_ZhIpNetToMediaIfIndex_Type=InterfaceIndex
_ZhIpNetToMediaIfIndex_Object=MibTableColumn
zhIpNetToMediaIfIndex=_ZhIpNetToMediaIfIndex_Object((1,3,6,1,4,1,5504,4,1,4,4,1,1),_ZhIpNetToMediaIfIndex_Type())
zhIpNetToMediaIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:zhIpNetToMediaIfIndex.setStatus(_A)
_ZhIpNetToMediaNetAddress_Type=IpAddress
_ZhIpNetToMediaNetAddress_Object=MibTableColumn
zhIpNetToMediaNetAddress=_ZhIpNetToMediaNetAddress_Object((1,3,6,1,4,1,5504,4,1,4,4,1,2),_ZhIpNetToMediaNetAddress_Type())
zhIpNetToMediaNetAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:zhIpNetToMediaNetAddress.setStatus(_A)
_ZhIpNetToMediaPhysAddress_Type=PhysAddress
_ZhIpNetToMediaPhysAddress_Object=MibTableColumn
zhIpNetToMediaPhysAddress=_ZhIpNetToMediaPhysAddress_Object((1,3,6,1,4,1,5504,4,1,4,4,1,3),_ZhIpNetToMediaPhysAddress_Type())
zhIpNetToMediaPhysAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:zhIpNetToMediaPhysAddress.setStatus(_A)
class _ZhIpNetToMediaType_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('invalid',2),('dynamic',3),('static',4)))
_ZhIpNetToMediaType_Type.__name__=_C
_ZhIpNetToMediaType_Object=MibTableColumn
zhIpNetToMediaType=_ZhIpNetToMediaType_Object((1,3,6,1,4,1,5504,4,1,4,4,1,4),_ZhIpNetToMediaType_Type())
zhIpNetToMediaType.setMaxAccess(_E)
if mibBuilder.loadTexts:zhIpNetToMediaType.setStatus(_A)
_ZhIpNetToMediaRowStatus_Type=ZhoneRowStatus
_ZhIpNetToMediaRowStatus_Object=MibTableColumn
zhIpNetToMediaRowStatus=_ZhIpNetToMediaRowStatus_Object((1,3,6,1,4,1,5504,4,1,4,4,1,5),_ZhIpNetToMediaRowStatus_Type())
zhIpNetToMediaRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:zhIpNetToMediaRowStatus.setStatus(_A)
rdEntry.registerAugmentions((_D,_J))
zhoneIpEntry.setIndexNames(*rdEntry.getIndexNames())
mibBuilder.exportSymbols(_D,**{'ip':ip,'zhoneIpTable':zhoneIpTable,_J:zhoneIpEntry,'zhIpForwarding':zhIpForwarding,'zhIpDefaultTTL':zhIpDefaultTTL,'zhIpInReceives':zhIpInReceives,'zhIpInHdrErrors':zhIpInHdrErrors,'zhIpInAddrErrors':zhIpInAddrErrors,'zhIpForwDatagrams':zhIpForwDatagrams,'zhIpInUnknownProtos':zhIpInUnknownProtos,'zhIpInDiscards':zhIpInDiscards,'zhIpInDelivers':zhIpInDelivers,'zhIpOutRequests':zhIpOutRequests,'zhIpOutDiscards':zhIpOutDiscards,'zhIpOutNoRoutes':zhIpOutNoRoutes,'zhIpReasmTimeout':zhIpReasmTimeout,'zhIpReasmReqds':zhIpReasmReqds,'zhIpReasmOKs':zhIpReasmOKs,'zhIpReasmFails':zhIpReasmFails,'zhIpFragOKs':zhIpFragOKs,'zhIpFragFails':zhIpFragFails,'zhIpFragCreates':zhIpFragCreates,'zhIpRoutingDiscards':zhIpRoutingDiscards,'zhoneIpNetToMediaTable':zhoneIpNetToMediaTable,'zhoneIpNetToMediaEntry':zhoneIpNetToMediaEntry,_G:zhIpNetToMediaIfIndex,_H:zhIpNetToMediaNetAddress,'zhIpNetToMediaPhysAddress':zhIpNetToMediaPhysAddress,'zhIpNetToMediaType':zhIpNetToMediaType,'zhIpNetToMediaRowStatus':zhIpNetToMediaRowStatus,'comIpIp':comIpIp})