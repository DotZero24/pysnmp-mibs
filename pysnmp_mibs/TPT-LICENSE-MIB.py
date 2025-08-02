_E='licenseEntryIndex'
_D='TPT-LICENSE-MIB'
_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tpt_tpa_objs,=mibBuilder.importSymbols('TPT-TPAMIBS-MIB','tpt-tpa-objs')
tpt_license_objs=ModuleIdentity((1,3,6,1,4,1,10734,3,3,2,15))
if mibBuilder.loadTexts:tpt_license_objs.setRevisions(('2016-05-25 18:54',))
class LicenseStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('info',0),('ok',1),('warning',2),('error',3)))
class LicenseAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('allow',0),('deny',1)))
_LicenseTable_Object=MibTable
licenseTable=_LicenseTable_Object((1,3,6,1,4,1,10734,3,3,2,15,1))
if mibBuilder.loadTexts:licenseTable.setStatus(_A)
_LicenseEntry_Object=MibTableRow
licenseEntry=_LicenseEntry_Object((1,3,6,1,4,1,10734,3,3,2,15,1,1))
licenseEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:licenseEntry.setStatus(_A)
_LicenseEntryIndex_Type=Unsigned32
_LicenseEntryIndex_Object=MibTableColumn
licenseEntryIndex=_LicenseEntryIndex_Object((1,3,6,1,4,1,10734,3,3,2,15,1,1,1),_LicenseEntryIndex_Type())
licenseEntryIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:licenseEntryIndex.setStatus(_A)
class _LicenseEntryFeature_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_LicenseEntryFeature_Type.__name__=_C
_LicenseEntryFeature_Object=MibTableColumn
licenseEntryFeature=_LicenseEntryFeature_Object((1,3,6,1,4,1,10734,3,3,2,15,1,1,2),_LicenseEntryFeature_Type())
licenseEntryFeature.setMaxAccess(_B)
if mibBuilder.loadTexts:licenseEntryFeature.setStatus(_A)
_LicenseEntryStatus_Type=LicenseStatus
_LicenseEntryStatus_Object=MibTableColumn
licenseEntryStatus=_LicenseEntryStatus_Object((1,3,6,1,4,1,10734,3,3,2,15,1,1,3),_LicenseEntryStatus_Type())
licenseEntryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:licenseEntryStatus.setStatus(_A)
_LicenseEntryAction_Type=LicenseAction
_LicenseEntryAction_Object=MibTableColumn
licenseEntryAction=_LicenseEntryAction_Object((1,3,6,1,4,1,10734,3,3,2,15,1,1,4),_LicenseEntryAction_Type())
licenseEntryAction.setMaxAccess(_B)
if mibBuilder.loadTexts:licenseEntryAction.setStatus(_A)
class _LicenseEntryExpiry_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_LicenseEntryExpiry_Type.__name__=_C
_LicenseEntryExpiry_Object=MibTableColumn
licenseEntryExpiry=_LicenseEntryExpiry_Object((1,3,6,1,4,1,10734,3,3,2,15,1,1,5),_LicenseEntryExpiry_Type())
licenseEntryExpiry.setMaxAccess(_B)
if mibBuilder.loadTexts:licenseEntryExpiry.setStatus(_A)
class _LicenseEntryDetails_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LicenseEntryDetails_Type.__name__=_C
_LicenseEntryDetails_Object=MibTableColumn
licenseEntryDetails=_LicenseEntryDetails_Object((1,3,6,1,4,1,10734,3,3,2,15,1,1,6),_LicenseEntryDetails_Type())
licenseEntryDetails.setMaxAccess(_B)
if mibBuilder.loadTexts:licenseEntryDetails.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'LicenseStatus':LicenseStatus,'LicenseAction':LicenseAction,'tpt-license-objs':tpt_license_objs,'licenseTable':licenseTable,'licenseEntry':licenseEntry,_E:licenseEntryIndex,'licenseEntryFeature':licenseEntryFeature,'licenseEntryStatus':licenseEntryStatus,'licenseEntryAction':licenseEntryAction,'licenseEntryExpiry':licenseEntryExpiry,'licenseEntryDetails':licenseEntryDetails})