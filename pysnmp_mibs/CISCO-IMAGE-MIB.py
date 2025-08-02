_F='ciscoImageMIBGroup'
_E='ciscoImageString'
_D='ciscoImageIndex'
_C='Integer32'
_B='CISCO-IMAGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoImageMIB=ModuleIdentity((1,3,6,1,4,1,9,9,25))
if mibBuilder.loadTexts:ciscoImageMIB.setRevisions(('1995-08-15 00:00','1995-01-16 00:00'))
_CiscoImageMIBObjects_ObjectIdentity=ObjectIdentity
ciscoImageMIBObjects=_CiscoImageMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,25,1))
_CiscoImageTable_Object=MibTable
ciscoImageTable=_CiscoImageTable_Object((1,3,6,1,4,1,9,9,25,1,1))
if mibBuilder.loadTexts:ciscoImageTable.setStatus(_A)
_CiscoImageEntry_Object=MibTableRow
ciscoImageEntry=_CiscoImageEntry_Object((1,3,6,1,4,1,9,9,25,1,1,1))
ciscoImageEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:ciscoImageEntry.setStatus(_A)
class _CiscoImageIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CiscoImageIndex_Type.__name__=_C
_CiscoImageIndex_Object=MibTableColumn
ciscoImageIndex=_CiscoImageIndex_Object((1,3,6,1,4,1,9,9,25,1,1,1,1),_CiscoImageIndex_Type())
ciscoImageIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ciscoImageIndex.setStatus(_A)
_CiscoImageString_Type=DisplayString
_CiscoImageString_Object=MibTableColumn
ciscoImageString=_CiscoImageString_Object((1,3,6,1,4,1,9,9,25,1,1,1,2),_CiscoImageString_Type())
ciscoImageString.setMaxAccess('read-only')
if mibBuilder.loadTexts:ciscoImageString.setStatus(_A)
_CiscoImageMIBConformance_ObjectIdentity=ObjectIdentity
ciscoImageMIBConformance=_CiscoImageMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,25,2))
_CiscoImageMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoImageMIBCompliances=_CiscoImageMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,25,2,1))
_CiscoImageMIBGroups_ObjectIdentity=ObjectIdentity
ciscoImageMIBGroups=_CiscoImageMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,25,2,2))
ciscoImageMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,25,2,2,1))
ciscoImageMIBGroup.setObjects((_B,_E))
if mibBuilder.loadTexts:ciscoImageMIBGroup.setStatus(_A)
ciscoImageMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,25,2,1,1))
ciscoImageMIBCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:ciscoImageMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoImageMIB':ciscoImageMIB,'ciscoImageMIBObjects':ciscoImageMIBObjects,'ciscoImageTable':ciscoImageTable,'ciscoImageEntry':ciscoImageEntry,_D:ciscoImageIndex,_E:ciscoImageString,'ciscoImageMIBConformance':ciscoImageMIBConformance,'ciscoImageMIBCompliances':ciscoImageMIBCompliances,'ciscoImageMIBCompliance':ciscoImageMIBCompliance,'ciscoImageMIBGroups':ciscoImageMIBGroups,_F:ciscoImageMIBGroup})