_G='fsCapwapMulticastMIBGroup'
_F='fsCapwapMulticastGroup'
_E='fsCapwapMulticastWorkingMode'
_D='read-write'
_C='Integer32'
_B='FS-CAPWAP-MULTICAST-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsCapwapMulticastMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,59))
if mibBuilder.loadTexts:fsCapwapMulticastMIB.setRevisions(('2009-10-22 00:00',))
_FsCapwapMulticastMIBObjects_ObjectIdentity=ObjectIdentity
fsCapwapMulticastMIBObjects=_FsCapwapMulticastMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,59,1))
class _FsCapwapMulticastWorkingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unicast',1),('multicast',2)))
_FsCapwapMulticastWorkingMode_Type.__name__=_C
_FsCapwapMulticastWorkingMode_Object=MibScalar
fsCapwapMulticastWorkingMode=_FsCapwapMulticastWorkingMode_Object((1,3,6,1,4,1,52642,1,1,10,2,59,1,1),_FsCapwapMulticastWorkingMode_Type())
fsCapwapMulticastWorkingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCapwapMulticastWorkingMode.setStatus(_A)
_FsCapwapMulticastGroup_Type=IpAddress
_FsCapwapMulticastGroup_Object=MibScalar
fsCapwapMulticastGroup=_FsCapwapMulticastGroup_Object((1,3,6,1,4,1,52642,1,1,10,2,59,1,2),_FsCapwapMulticastGroup_Type())
fsCapwapMulticastGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCapwapMulticastGroup.setStatus(_A)
_FsCapwapMulticastMIBConformance_ObjectIdentity=ObjectIdentity
fsCapwapMulticastMIBConformance=_FsCapwapMulticastMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,59,2))
_FsCapwapMulticastMIBCompliances_ObjectIdentity=ObjectIdentity
fsCapwapMulticastMIBCompliances=_FsCapwapMulticastMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,59,2,1))
_FsCapwapMulticastMIBGroups_ObjectIdentity=ObjectIdentity
fsCapwapMulticastMIBGroups=_FsCapwapMulticastMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,59,2,2))
fsCapwapMulticastMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,59,2,2,1))
fsCapwapMulticastMIBGroup.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:fsCapwapMulticastMIBGroup.setStatus(_A)
fsCapwapMulticastMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,59,2,1,1))
fsCapwapMulticastMIBCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:fsCapwapMulticastMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsCapwapMulticastMIB':fsCapwapMulticastMIB,'fsCapwapMulticastMIBObjects':fsCapwapMulticastMIBObjects,_E:fsCapwapMulticastWorkingMode,_F:fsCapwapMulticastGroup,'fsCapwapMulticastMIBConformance':fsCapwapMulticastMIBConformance,'fsCapwapMulticastMIBCompliances':fsCapwapMulticastMIBCompliances,'fsCapwapMulticastMIBCompliance':fsCapwapMulticastMIBCompliance,'fsCapwapMulticastMIBGroups':fsCapwapMulticastMIBGroups,_G:fsCapwapMulticastMIBGroup})