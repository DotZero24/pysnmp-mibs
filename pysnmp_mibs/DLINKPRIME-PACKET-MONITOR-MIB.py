_C='Integer32'
_B='current'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero','ifIndex')
PortList,VlanId=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
dlinkPrimePktMonitorMIB=ModuleIdentity((1,3,6,1,4,1,171,15,10))
if mibBuilder.loadTexts:dlinkPrimePktMonitorMIB.setRevisions(('2014-06-03 00:00',))
_DpPktMonMIBNotifications_ObjectIdentity=ObjectIdentity
dpPktMonMIBNotifications=_DpPktMonMIBNotifications_ObjectIdentity((1,3,6,1,4,1,171,15,10,0))
_DpPktMonMIBObjects_ObjectIdentity=ObjectIdentity
dpPktMonMIBObjects=_DpPktMonMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,15,10,1))
_DpPktMonDstPort_Type=Integer32
_DpPktMonDstPort_Object=MibScalar
dpPktMonDstPort=_DpPktMonDstPort_Object((1,3,6,1,4,1,171,15,10,1,1),_DpPktMonDstPort_Type())
dpPktMonDstPort.setMaxAccess(_A)
if mibBuilder.loadTexts:dpPktMonDstPort.setStatus(_B)
class _DpPktMonMirrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('disable',0),('rx',1),('tx',2),('both',3)))
_DpPktMonMirrorType_Type.__name__=_C
_DpPktMonMirrorType_Object=MibScalar
dpPktMonMirrorType=_DpPktMonMirrorType_Object((1,3,6,1,4,1,171,15,10,1,2),_DpPktMonMirrorType_Type())
dpPktMonMirrorType.setMaxAccess(_A)
if mibBuilder.loadTexts:dpPktMonMirrorType.setStatus(_B)
_DpPktMonSrcPort_Type=PortList
_DpPktMonSrcPort_Object=MibScalar
dpPktMonSrcPort=_DpPktMonSrcPort_Object((1,3,6,1,4,1,171,15,10,1,3),_DpPktMonSrcPort_Type())
dpPktMonSrcPort.setMaxAccess(_A)
if mibBuilder.loadTexts:dpPktMonSrcPort.setStatus(_B)
_DpPktMonMIBConformance_ObjectIdentity=ObjectIdentity
dpPktMonMIBConformance=_DpPktMonMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,15,10,2))
_DpPktMonMIBCompliances_ObjectIdentity=ObjectIdentity
dpPktMonMIBCompliances=_DpPktMonMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,15,10,2,1))
mibBuilder.exportSymbols('DLINKPRIME-PACKET-MONITOR-MIB',**{'dlinkPrimePktMonitorMIB':dlinkPrimePktMonitorMIB,'dpPktMonMIBNotifications':dpPktMonMIBNotifications,'dpPktMonMIBObjects':dpPktMonMIBObjects,'dpPktMonDstPort':dpPktMonDstPort,'dpPktMonMirrorType':dpPktMonMirrorType,'dpPktMonSrcPort':dpPktMonSrcPort,'dpPktMonMIBConformance':dpPktMonMIBConformance,'dpPktMonMIBCompliances':dpPktMonMIBCompliances})