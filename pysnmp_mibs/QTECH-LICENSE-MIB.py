_H='qtechLicenseMIBGroup'
_G='qtechLicenseValue'
_F='qtechLicenseString'
_E='qtechShowLicense'
_D='qtechLicenseIndex'
_C='read-only'
_B='QTECH-LICENSE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
qtechLicenseMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,57))
if mibBuilder.loadTexts:qtechLicenseMIB.setRevisions(('2009-09-18 00:00',))
_QtechLicenseMIBObjects_ObjectIdentity=ObjectIdentity
qtechLicenseMIBObjects=_QtechLicenseMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,57,1))
_QtechShowLicense_Type=Integer32
_QtechShowLicense_Object=MibScalar
qtechShowLicense=_QtechShowLicense_Object((1,3,6,1,4,1,27514,1,1,10,2,57,1,1),_QtechShowLicense_Type())
qtechShowLicense.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechShowLicense.setStatus(_A)
_QtechLicenseTable_Object=MibTable
qtechLicenseTable=_QtechLicenseTable_Object((1,3,6,1,4,1,27514,1,1,10,2,57,1,2))
if mibBuilder.loadTexts:qtechLicenseTable.setStatus(_A)
_QtechLicenseEntry_Object=MibTableRow
qtechLicenseEntry=_QtechLicenseEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,57,1,2,1))
qtechLicenseEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:qtechLicenseEntry.setStatus(_A)
_QtechLicenseIndex_Type=Integer32
_QtechLicenseIndex_Object=MibTableColumn
qtechLicenseIndex=_QtechLicenseIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,57,1,2,1,1),_QtechLicenseIndex_Type())
qtechLicenseIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:qtechLicenseIndex.setStatus(_A)
_QtechLicenseString_Type=DisplayString
_QtechLicenseString_Object=MibTableColumn
qtechLicenseString=_QtechLicenseString_Object((1,3,6,1,4,1,27514,1,1,10,2,57,1,2,1,2),_QtechLicenseString_Type())
qtechLicenseString.setMaxAccess('read-write')
if mibBuilder.loadTexts:qtechLicenseString.setStatus(_A)
_QtechLicenseValue_Type=Integer32
_QtechLicenseValue_Object=MibTableColumn
qtechLicenseValue=_QtechLicenseValue_Object((1,3,6,1,4,1,27514,1,1,10,2,57,1,2,1,3),_QtechLicenseValue_Type())
qtechLicenseValue.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLicenseValue.setStatus(_A)
_QtechLicenseMIBConformance_ObjectIdentity=ObjectIdentity
qtechLicenseMIBConformance=_QtechLicenseMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,57,2))
_QtechLicenseMIBCompliances_ObjectIdentity=ObjectIdentity
qtechLicenseMIBCompliances=_QtechLicenseMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,57,2,1))
_QtechLicenseMIBGroups_ObjectIdentity=ObjectIdentity
qtechLicenseMIBGroups=_QtechLicenseMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,57,2,2))
qtechLicenseMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,57,2,2,1))
qtechLicenseMIBGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:qtechLicenseMIBGroup.setStatus(_A)
qtechLicenseMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,57,2,1,1))
qtechLicenseMIBCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:qtechLicenseMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechLicenseMIB':qtechLicenseMIB,'qtechLicenseMIBObjects':qtechLicenseMIBObjects,_E:qtechShowLicense,'qtechLicenseTable':qtechLicenseTable,'qtechLicenseEntry':qtechLicenseEntry,_D:qtechLicenseIndex,_F:qtechLicenseString,_G:qtechLicenseValue,'qtechLicenseMIBConformance':qtechLicenseMIBConformance,'qtechLicenseMIBCompliances':qtechLicenseMIBCompliances,'qtechLicenseMIBCompliance':qtechLicenseMIBCompliance,'qtechLicenseMIBGroups':qtechLicenseMIBGroups,_H:qtechLicenseMIBGroup})