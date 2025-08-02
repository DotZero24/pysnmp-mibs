_G='fsCapwapMulticast6MIBGroup'
_F='fsCapwapMulticast6Group'
_E='fsCapwapMulticast6WorkingMode'
_D='read-write'
_C='Integer32'
_B='FS-CAPWAP-MULTICAST6-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
InetAddress,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsCapwapMulticast6MIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,85))
if mibBuilder.loadTexts:fsCapwapMulticast6MIB.setRevisions(('2010-05-20 00:00',))
_FsCapwapMulticast6MIBObjects_ObjectIdentity=ObjectIdentity
fsCapwapMulticast6MIBObjects=_FsCapwapMulticast6MIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,85,1))
class _FsCapwapMulticast6WorkingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disabled',1),('unicast',2),('multicast',3)))
_FsCapwapMulticast6WorkingMode_Type.__name__=_C
_FsCapwapMulticast6WorkingMode_Object=MibScalar
fsCapwapMulticast6WorkingMode=_FsCapwapMulticast6WorkingMode_Object((1,3,6,1,4,1,52642,1,1,10,2,85,1,1),_FsCapwapMulticast6WorkingMode_Type())
fsCapwapMulticast6WorkingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCapwapMulticast6WorkingMode.setStatus(_A)
_FsCapwapMulticast6Group_Type=InetAddress
_FsCapwapMulticast6Group_Object=MibScalar
fsCapwapMulticast6Group=_FsCapwapMulticast6Group_Object((1,3,6,1,4,1,52642,1,1,10,2,85,1,2),_FsCapwapMulticast6Group_Type())
fsCapwapMulticast6Group.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCapwapMulticast6Group.setStatus(_A)
_FsCapwapMulticast6MIBConformance_ObjectIdentity=ObjectIdentity
fsCapwapMulticast6MIBConformance=_FsCapwapMulticast6MIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,85,2))
_FsCapwapMulticast6MIBCompliances_ObjectIdentity=ObjectIdentity
fsCapwapMulticast6MIBCompliances=_FsCapwapMulticast6MIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,85,2,1))
_FsCapwapMulticast6MIBGroups_ObjectIdentity=ObjectIdentity
fsCapwapMulticast6MIBGroups=_FsCapwapMulticast6MIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,85,2,2))
fsCapwapMulticast6MIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,85,2,2,1))
fsCapwapMulticast6MIBGroup.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:fsCapwapMulticast6MIBGroup.setStatus(_A)
fsCapwapMulticast6MIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,85,2,1,1))
fsCapwapMulticast6MIBCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:fsCapwapMulticast6MIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsCapwapMulticast6MIB':fsCapwapMulticast6MIB,'fsCapwapMulticast6MIBObjects':fsCapwapMulticast6MIBObjects,_E:fsCapwapMulticast6WorkingMode,_F:fsCapwapMulticast6Group,'fsCapwapMulticast6MIBConformance':fsCapwapMulticast6MIBConformance,'fsCapwapMulticast6MIBCompliances':fsCapwapMulticast6MIBCompliances,'fsCapwapMulticast6MIBCompliance':fsCapwapMulticast6MIBCompliance,'fsCapwapMulticast6MIBGroups':fsCapwapMulticast6MIBGroups,_G:fsCapwapMulticast6MIBGroup})