_G='qtechCapwapMulticastMIBGroup'
_F='qtechCapwapMulticastGroup'
_E='qtechCapwapMulticastWorkingMode'
_D='read-write'
_C='Integer32'
_B='QTECH-CAPWAP-MULTICAST-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
qtechCapwapMulticastMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,59))
if mibBuilder.loadTexts:qtechCapwapMulticastMIB.setRevisions(('2009-10-22 00:00',))
_QtechCapwapMulticastMIBObjects_ObjectIdentity=ObjectIdentity
qtechCapwapMulticastMIBObjects=_QtechCapwapMulticastMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,59,1))
class _QtechCapwapMulticastWorkingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unicast',1),('multicast',2)))
_QtechCapwapMulticastWorkingMode_Type.__name__=_C
_QtechCapwapMulticastWorkingMode_Object=MibScalar
qtechCapwapMulticastWorkingMode=_QtechCapwapMulticastWorkingMode_Object((1,3,6,1,4,1,27514,1,1,10,2,59,1,1),_QtechCapwapMulticastWorkingMode_Type())
qtechCapwapMulticastWorkingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechCapwapMulticastWorkingMode.setStatus(_A)
_QtechCapwapMulticastGroup_Type=IpAddress
_QtechCapwapMulticastGroup_Object=MibScalar
qtechCapwapMulticastGroup=_QtechCapwapMulticastGroup_Object((1,3,6,1,4,1,27514,1,1,10,2,59,1,2),_QtechCapwapMulticastGroup_Type())
qtechCapwapMulticastGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechCapwapMulticastGroup.setStatus(_A)
_QtechCapwapMulticastMIBConformance_ObjectIdentity=ObjectIdentity
qtechCapwapMulticastMIBConformance=_QtechCapwapMulticastMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,59,2))
_QtechCapwapMulticastMIBCompliances_ObjectIdentity=ObjectIdentity
qtechCapwapMulticastMIBCompliances=_QtechCapwapMulticastMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,59,2,1))
_QtechCapwapMulticastMIBGroups_ObjectIdentity=ObjectIdentity
qtechCapwapMulticastMIBGroups=_QtechCapwapMulticastMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,59,2,2))
qtechCapwapMulticastMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,59,2,2,1))
qtechCapwapMulticastMIBGroup.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:qtechCapwapMulticastMIBGroup.setStatus(_A)
qtechCapwapMulticastMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,59,2,1,1))
qtechCapwapMulticastMIBCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:qtechCapwapMulticastMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechCapwapMulticastMIB':qtechCapwapMulticastMIB,'qtechCapwapMulticastMIBObjects':qtechCapwapMulticastMIBObjects,_E:qtechCapwapMulticastWorkingMode,_F:qtechCapwapMulticastGroup,'qtechCapwapMulticastMIBConformance':qtechCapwapMulticastMIBConformance,'qtechCapwapMulticastMIBCompliances':qtechCapwapMulticastMIBCompliances,'qtechCapwapMulticastMIBCompliance':qtechCapwapMulticastMIBCompliance,'qtechCapwapMulticastMIBGroups':qtechCapwapMulticastMIBGroups,_G:qtechCapwapMulticastMIBGroup})