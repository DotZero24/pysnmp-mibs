_H='fsvplsLdpPwIndex'
_G='FS-VPLS-LDP-MIB'
_F='Unsigned32'
_E='Integer32'
_D='fsvplsConfigIndex'
_C='FS-VPLS-GENERIC-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
fsvplsConfigIndex,fsvplsPwBindIndex=mibBuilder.importSymbols(_C,_D,'fsvplsPwBindIndex')
IANAPwCapabilities,IANAPwPsnTypeTC,IANAPwTypeTC=mibBuilder.importSymbols('IANA-PWE3-MIB','IANAPwCapabilities','IANAPwPsnTypeTC','IANAPwTypeTC')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso','transmission')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
fsvplsLdpDraft01MIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,78))
if mibBuilder.loadTexts:fsvplsLdpDraft01MIB.setRevisions(('2010-04-28 12:00',))
_FsvplsLdpNotifications_ObjectIdentity=ObjectIdentity
fsvplsLdpNotifications=_FsvplsLdpNotifications_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,78,0))
_FsvplsLdpObjects_ObjectIdentity=ObjectIdentity
fsvplsLdpObjects=_FsvplsLdpObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,78,1))
_FsvplsLdpConfigTable_Object=MibTable
fsvplsLdpConfigTable=_FsvplsLdpConfigTable_Object((1,3,6,1,4,1,52642,1,1,10,2,78,1,1))
if mibBuilder.loadTexts:fsvplsLdpConfigTable.setStatus(_A)
_FsvplsLdpConfigEntry_Object=MibTableRow
fsvplsLdpConfigEntry=_FsvplsLdpConfigEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,78,1,1,1))
fsvplsLdpConfigEntry.setIndexNames((0,_C,_D),(0,_G,_H))
if mibBuilder.loadTexts:fsvplsLdpConfigEntry.setStatus(_A)
_FsvplsLdpPwIndex_Type=Unsigned32
_FsvplsLdpPwIndex_Object=MibTableColumn
fsvplsLdpPwIndex=_FsvplsLdpPwIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,78,1,1,1,1),_FsvplsLdpPwIndex_Type())
fsvplsLdpPwIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fsvplsLdpPwIndex.setStatus(_A)
_FsvplsLdpPeerAddr_Type=InetAddress
_FsvplsLdpPeerAddr_Object=MibTableColumn
fsvplsLdpPeerAddr=_FsvplsLdpPeerAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,78,1,1,1,2),_FsvplsLdpPeerAddr_Type())
fsvplsLdpPeerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsvplsLdpPeerAddr.setStatus(_A)
class _FsvplsLdpPwId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsvplsLdpPwId_Type.__name__=_F
_FsvplsLdpPwId_Object=MibTableColumn
fsvplsLdpPwId=_FsvplsLdpPwId_Object((1,3,6,1,4,1,52642,1,1,10,2,78,1,1,1,3),_FsvplsLdpPwId_Type())
fsvplsLdpPwId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsvplsLdpPwId.setStatus(_A)
class _FsvplsPwType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mesh',1),('spoke',2)))
_FsvplsPwType_Type.__name__=_E
_FsvplsPwType_Object=MibTableColumn
fsvplsPwType=_FsvplsPwType_Object((1,3,6,1,4,1,52642,1,1,10,2,78,1,1,1,4),_FsvplsPwType_Type())
fsvplsPwType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsvplsPwType.setStatus(_A)
_FsvplsPwEncapType_Type=IANAPwTypeTC
_FsvplsPwEncapType_Object=MibTableColumn
fsvplsPwEncapType=_FsvplsPwEncapType_Object((1,3,6,1,4,1,52642,1,1,10,2,78,1,1,1,5),_FsvplsPwEncapType_Type())
fsvplsPwEncapType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsvplsPwEncapType.setStatus(_A)
_FsvplsLdpNeighborRowStatus_Type=RowStatus
_FsvplsLdpNeighborRowStatus_Object=MibTableColumn
fsvplsLdpNeighborRowStatus=_FsvplsLdpNeighborRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,78,1,1,1,6),_FsvplsLdpNeighborRowStatus_Type())
fsvplsLdpNeighborRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsvplsLdpNeighborRowStatus.setStatus(_A)
_FsvplsLdpConformance_ObjectIdentity=ObjectIdentity
fsvplsLdpConformance=_FsvplsLdpConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,78,2))
mibBuilder.exportSymbols(_G,**{'fsvplsLdpDraft01MIB':fsvplsLdpDraft01MIB,'fsvplsLdpNotifications':fsvplsLdpNotifications,'fsvplsLdpObjects':fsvplsLdpObjects,'fsvplsLdpConfigTable':fsvplsLdpConfigTable,'fsvplsLdpConfigEntry':fsvplsLdpConfigEntry,_H:fsvplsLdpPwIndex,'fsvplsLdpPeerAddr':fsvplsLdpPeerAddr,'fsvplsLdpPwId':fsvplsLdpPwId,'fsvplsPwType':fsvplsPwType,'fsvplsPwEncapType':fsvplsPwEncapType,'fsvplsLdpNeighborRowStatus':fsvplsLdpNeighborRowStatus,'fsvplsLdpConformance':fsvplsLdpConformance})