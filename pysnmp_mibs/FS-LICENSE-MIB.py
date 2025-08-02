_H='fsLicenseMIBGroup'
_G='fsLicenseValue'
_F='fsLicenseString'
_E='fsShowLicense'
_D='fsLicenseIndex'
_C='read-only'
_B='FS-LICENSE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsLicenseMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,57))
if mibBuilder.loadTexts:fsLicenseMIB.setRevisions(('2009-09-18 00:00',))
_FsLicenseMIBObjects_ObjectIdentity=ObjectIdentity
fsLicenseMIBObjects=_FsLicenseMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,57,1))
_FsShowLicense_Type=Integer32
_FsShowLicense_Object=MibScalar
fsShowLicense=_FsShowLicense_Object((1,3,6,1,4,1,52642,1,1,10,2,57,1,1),_FsShowLicense_Type())
fsShowLicense.setMaxAccess(_C)
if mibBuilder.loadTexts:fsShowLicense.setStatus(_A)
_FsLicenseTable_Object=MibTable
fsLicenseTable=_FsLicenseTable_Object((1,3,6,1,4,1,52642,1,1,10,2,57,1,2))
if mibBuilder.loadTexts:fsLicenseTable.setStatus(_A)
_FsLicenseEntry_Object=MibTableRow
fsLicenseEntry=_FsLicenseEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,57,1,2,1))
fsLicenseEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:fsLicenseEntry.setStatus(_A)
_FsLicenseIndex_Type=Integer32
_FsLicenseIndex_Object=MibTableColumn
fsLicenseIndex=_FsLicenseIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,57,1,2,1,1),_FsLicenseIndex_Type())
fsLicenseIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fsLicenseIndex.setStatus(_A)
_FsLicenseString_Type=DisplayString
_FsLicenseString_Object=MibTableColumn
fsLicenseString=_FsLicenseString_Object((1,3,6,1,4,1,52642,1,1,10,2,57,1,2,1,2),_FsLicenseString_Type())
fsLicenseString.setMaxAccess('read-write')
if mibBuilder.loadTexts:fsLicenseString.setStatus(_A)
_FsLicenseValue_Type=Integer32
_FsLicenseValue_Object=MibTableColumn
fsLicenseValue=_FsLicenseValue_Object((1,3,6,1,4,1,52642,1,1,10,2,57,1,2,1,3),_FsLicenseValue_Type())
fsLicenseValue.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLicenseValue.setStatus(_A)
_FsLicenseMIBConformance_ObjectIdentity=ObjectIdentity
fsLicenseMIBConformance=_FsLicenseMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,57,2))
_FsLicenseMIBCompliances_ObjectIdentity=ObjectIdentity
fsLicenseMIBCompliances=_FsLicenseMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,57,2,1))
_FsLicenseMIBGroups_ObjectIdentity=ObjectIdentity
fsLicenseMIBGroups=_FsLicenseMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,57,2,2))
fsLicenseMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,57,2,2,1))
fsLicenseMIBGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:fsLicenseMIBGroup.setStatus(_A)
fsLicenseMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,57,2,1,1))
fsLicenseMIBCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:fsLicenseMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsLicenseMIB':fsLicenseMIB,'fsLicenseMIBObjects':fsLicenseMIBObjects,_E:fsShowLicense,'fsLicenseTable':fsLicenseTable,'fsLicenseEntry':fsLicenseEntry,_D:fsLicenseIndex,_F:fsLicenseString,_G:fsLicenseValue,'fsLicenseMIBConformance':fsLicenseMIBConformance,'fsLicenseMIBCompliances':fsLicenseMIBCompliances,'fsLicenseMIBCompliance':fsLicenseMIBCompliance,'fsLicenseMIBGroups':fsLicenseMIBGroups,_H:fsLicenseMIBGroup})