_G='qtechCapwapMulticast6MIBGroup'
_F='qtechCapwapMulticast6Group'
_E='qtechCapwapMulticast6WorkingMode'
_D='read-write'
_C='Integer32'
_B='QTECH-CAPWAP-MULTICAST6-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
qtechCapwapMulticast6MIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,85))
if mibBuilder.loadTexts:qtechCapwapMulticast6MIB.setRevisions(('2010-05-20 00:00',))
_QtechCapwapMulticast6MIBObjects_ObjectIdentity=ObjectIdentity
qtechCapwapMulticast6MIBObjects=_QtechCapwapMulticast6MIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,85,1))
class _QtechCapwapMulticast6WorkingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disabled',1),('unicast',2),('multicast',3)))
_QtechCapwapMulticast6WorkingMode_Type.__name__=_C
_QtechCapwapMulticast6WorkingMode_Object=MibScalar
qtechCapwapMulticast6WorkingMode=_QtechCapwapMulticast6WorkingMode_Object((1,3,6,1,4,1,27514,1,1,10,2,85,1,1),_QtechCapwapMulticast6WorkingMode_Type())
qtechCapwapMulticast6WorkingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechCapwapMulticast6WorkingMode.setStatus(_A)
_QtechCapwapMulticast6Group_Type=InetAddress
_QtechCapwapMulticast6Group_Object=MibScalar
qtechCapwapMulticast6Group=_QtechCapwapMulticast6Group_Object((1,3,6,1,4,1,27514,1,1,10,2,85,1,2),_QtechCapwapMulticast6Group_Type())
qtechCapwapMulticast6Group.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechCapwapMulticast6Group.setStatus(_A)
_QtechCapwapMulticast6MIBConformance_ObjectIdentity=ObjectIdentity
qtechCapwapMulticast6MIBConformance=_QtechCapwapMulticast6MIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,85,2))
_QtechCapwapMulticast6MIBCompliances_ObjectIdentity=ObjectIdentity
qtechCapwapMulticast6MIBCompliances=_QtechCapwapMulticast6MIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,85,2,1))
_QtechCapwapMulticast6MIBGroups_ObjectIdentity=ObjectIdentity
qtechCapwapMulticast6MIBGroups=_QtechCapwapMulticast6MIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,85,2,2))
qtechCapwapMulticast6MIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,85,2,2,1))
qtechCapwapMulticast6MIBGroup.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:qtechCapwapMulticast6MIBGroup.setStatus(_A)
qtechCapwapMulticast6MIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,85,2,1,1))
qtechCapwapMulticast6MIBCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:qtechCapwapMulticast6MIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechCapwapMulticast6MIB':qtechCapwapMulticast6MIB,'qtechCapwapMulticast6MIBObjects':qtechCapwapMulticast6MIBObjects,_E:qtechCapwapMulticast6WorkingMode,_F:qtechCapwapMulticast6Group,'qtechCapwapMulticast6MIBConformance':qtechCapwapMulticast6MIBConformance,'qtechCapwapMulticast6MIBCompliances':qtechCapwapMulticast6MIBCompliances,'qtechCapwapMulticast6MIBCompliance':qtechCapwapMulticast6MIBCompliance,'qtechCapwapMulticast6MIBGroups':qtechCapwapMulticast6MIBGroups,_G:qtechCapwapMulticast6MIBGroup})