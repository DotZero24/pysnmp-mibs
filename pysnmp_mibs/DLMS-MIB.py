_N='expired'
_M='active'
_L='read-write'
_K='OctetString'
_J='swDlmsStackLicenseAc'
_I='swDlmsLicenseAc'
_H='Integer32'
_G='swDlmsInstallAc'
_F='swDlmsStackLicenseModelName'
_E='swDlmsStackLicenseModelUnitId'
_D='swDlmsLicenseModelName'
_C='read-only'
_B='DLMS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
swDlmsMIB=ModuleIdentity((1,3,6,1,4,1,171,12,101))
_SwDlmsNotifications_ObjectIdentity=ObjectIdentity
swDlmsNotifications=_SwDlmsNotifications_ObjectIdentity((1,3,6,1,4,1,171,12,101,0))
_SwDlmsObjects_ObjectIdentity=ObjectIdentity
swDlmsObjects=_SwDlmsObjects_ObjectIdentity((1,3,6,1,4,1,171,12,101,1))
_SwDlmsGeneralGroup_ObjectIdentity=ObjectIdentity
swDlmsGeneralGroup=_SwDlmsGeneralGroup_ObjectIdentity((1,3,6,1,4,1,171,12,101,1,1))
class _SwDlmsInstallAc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_SwDlmsInstallAc_Type.__name__=_K
_SwDlmsInstallAc_Object=MibScalar
swDlmsInstallAc=_SwDlmsInstallAc_Object((1,3,6,1,4,1,171,12,101,1,1,1),_SwDlmsInstallAc_Type())
swDlmsInstallAc.setMaxAccess(_L)
if mibBuilder.loadTexts:swDlmsInstallAc.setStatus(_A)
class _SwDlmsInstallStackUnitId_Type(Integer32):defaultValue=0
_SwDlmsInstallStackUnitId_Type.__name__=_H
_SwDlmsInstallStackUnitId_Object=MibScalar
swDlmsInstallStackUnitId=_SwDlmsInstallStackUnitId_Object((1,3,6,1,4,1,171,12,101,1,1,2),_SwDlmsInstallStackUnitId_Type())
swDlmsInstallStackUnitId.setMaxAccess(_L)
if mibBuilder.loadTexts:swDlmsInstallStackUnitId.setStatus(_A)
_SwDlmsLicense_ObjectIdentity=ObjectIdentity
swDlmsLicense=_SwDlmsLicense_ObjectIdentity((1,3,6,1,4,1,171,12,101,1,2))
_SwDlmsLicenseModelTable_Object=MibTable
swDlmsLicenseModelTable=_SwDlmsLicenseModelTable_Object((1,3,6,1,4,1,171,12,101,1,2,1))
if mibBuilder.loadTexts:swDlmsLicenseModelTable.setStatus(_A)
_SwDlmsLicenseModelEntry_Object=MibTableRow
swDlmsLicenseModelEntry=_SwDlmsLicenseModelEntry_Object((1,3,6,1,4,1,171,12,101,1,2,1,1))
swDlmsLicenseModelEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:swDlmsLicenseModelEntry.setStatus(_A)
_SwDlmsLicenseModelName_Type=DisplayString
_SwDlmsLicenseModelName_Object=MibTableColumn
swDlmsLicenseModelName=_SwDlmsLicenseModelName_Object((1,3,6,1,4,1,171,12,101,1,2,1,1,1),_SwDlmsLicenseModelName_Type())
swDlmsLicenseModelName.setMaxAccess(_C)
if mibBuilder.loadTexts:swDlmsLicenseModelName.setStatus(_A)
_SwDlmsLicenseModelRemaining_Type=DisplayString
_SwDlmsLicenseModelRemaining_Object=MibTableColumn
swDlmsLicenseModelRemaining=_SwDlmsLicenseModelRemaining_Object((1,3,6,1,4,1,171,12,101,1,2,1,1,2),_SwDlmsLicenseModelRemaining_Type())
swDlmsLicenseModelRemaining.setMaxAccess(_C)
if mibBuilder.loadTexts:swDlmsLicenseModelRemaining.setStatus(_A)
_SwDlmsLicenseAcTable_Object=MibTable
swDlmsLicenseAcTable=_SwDlmsLicenseAcTable_Object((1,3,6,1,4,1,171,12,101,1,2,2))
if mibBuilder.loadTexts:swDlmsLicenseAcTable.setStatus(_A)
_SwDlmsLicenseAcEntry_Object=MibTableRow
swDlmsLicenseAcEntry=_SwDlmsLicenseAcEntry_Object((1,3,6,1,4,1,171,12,101,1,2,2,1))
swDlmsLicenseAcEntry.setIndexNames((0,_B,_D),(0,_B,_I))
if mibBuilder.loadTexts:swDlmsLicenseAcEntry.setStatus(_A)
_SwDlmsLicenseAc_Type=OctetString
_SwDlmsLicenseAc_Object=MibTableColumn
swDlmsLicenseAc=_SwDlmsLicenseAc_Object((1,3,6,1,4,1,171,12,101,1,2,2,1,1),_SwDlmsLicenseAc_Type())
swDlmsLicenseAc.setMaxAccess(_C)
if mibBuilder.loadTexts:swDlmsLicenseAc.setStatus(_A)
class _SwDlmsLicenseAcStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_SwDlmsLicenseAcStatus_Type.__name__=_H
_SwDlmsLicenseAcStatus_Object=MibTableColumn
swDlmsLicenseAcStatus=_SwDlmsLicenseAcStatus_Object((1,3,6,1,4,1,171,12,101,1,2,2,1,2),_SwDlmsLicenseAcStatus_Type())
swDlmsLicenseAcStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swDlmsLicenseAcStatus.setStatus(_A)
_SwDlmsStackLicense_ObjectIdentity=ObjectIdentity
swDlmsStackLicense=_SwDlmsStackLicense_ObjectIdentity((1,3,6,1,4,1,171,12,101,1,3))
_SwDlmsStackLicenseModelTable_Object=MibTable
swDlmsStackLicenseModelTable=_SwDlmsStackLicenseModelTable_Object((1,3,6,1,4,1,171,12,101,1,3,1))
if mibBuilder.loadTexts:swDlmsStackLicenseModelTable.setStatus(_A)
_SwDlmsStackLicenseModelEntry_Object=MibTableRow
swDlmsStackLicenseModelEntry=_SwDlmsStackLicenseModelEntry_Object((1,3,6,1,4,1,171,12,101,1,3,1,1))
swDlmsStackLicenseModelEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:swDlmsStackLicenseModelEntry.setStatus(_A)
_SwDlmsStackLicenseModelUnitId_Type=Integer32
_SwDlmsStackLicenseModelUnitId_Object=MibTableColumn
swDlmsStackLicenseModelUnitId=_SwDlmsStackLicenseModelUnitId_Object((1,3,6,1,4,1,171,12,101,1,3,1,1,1),_SwDlmsStackLicenseModelUnitId_Type())
swDlmsStackLicenseModelUnitId.setMaxAccess(_C)
if mibBuilder.loadTexts:swDlmsStackLicenseModelUnitId.setStatus(_A)
_SwDlmsStackLicenseModelName_Type=DisplayString
_SwDlmsStackLicenseModelName_Object=MibTableColumn
swDlmsStackLicenseModelName=_SwDlmsStackLicenseModelName_Object((1,3,6,1,4,1,171,12,101,1,3,1,1,2),_SwDlmsStackLicenseModelName_Type())
swDlmsStackLicenseModelName.setMaxAccess(_C)
if mibBuilder.loadTexts:swDlmsStackLicenseModelName.setStatus(_A)
_SwDlmsStackLicenseModelRemaining_Type=DisplayString
_SwDlmsStackLicenseModelRemaining_Object=MibTableColumn
swDlmsStackLicenseModelRemaining=_SwDlmsStackLicenseModelRemaining_Object((1,3,6,1,4,1,171,12,101,1,3,1,1,3),_SwDlmsStackLicenseModelRemaining_Type())
swDlmsStackLicenseModelRemaining.setMaxAccess(_C)
if mibBuilder.loadTexts:swDlmsStackLicenseModelRemaining.setStatus(_A)
_SwDlmsStackLicenseAcTable_Object=MibTable
swDlmsStackLicenseAcTable=_SwDlmsStackLicenseAcTable_Object((1,3,6,1,4,1,171,12,101,1,3,2))
if mibBuilder.loadTexts:swDlmsStackLicenseAcTable.setStatus(_A)
_SwDlmsStackLicenseAcEntry_Object=MibTableRow
swDlmsStackLicenseAcEntry=_SwDlmsStackLicenseAcEntry_Object((1,3,6,1,4,1,171,12,101,1,3,2,1))
swDlmsStackLicenseAcEntry.setIndexNames((0,_B,_E),(0,_B,_F),(0,_B,_J))
if mibBuilder.loadTexts:swDlmsStackLicenseAcEntry.setStatus(_A)
_SwDlmsStackLicenseAc_Type=OctetString
_SwDlmsStackLicenseAc_Object=MibTableColumn
swDlmsStackLicenseAc=_SwDlmsStackLicenseAc_Object((1,3,6,1,4,1,171,12,101,1,3,2,1,1),_SwDlmsStackLicenseAc_Type())
swDlmsStackLicenseAc.setMaxAccess(_C)
if mibBuilder.loadTexts:swDlmsStackLicenseAc.setStatus(_A)
class _SwDlmsStackLicenseAcStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_SwDlmsStackLicenseAcStatus_Type.__name__=_H
_SwDlmsStackLicenseAcStatus_Object=MibTableColumn
swDlmsStackLicenseAcStatus=_SwDlmsStackLicenseAcStatus_Object((1,3,6,1,4,1,171,12,101,1,3,2,1,2),_SwDlmsStackLicenseAcStatus_Type())
swDlmsStackLicenseAcStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swDlmsStackLicenseAcStatus.setStatus(_A)
swDlmsIllegalAc=NotificationType((1,3,6,1,4,1,171,12,101,0,1))
swDlmsIllegalAc.setObjects((_B,_G))
if mibBuilder.loadTexts:swDlmsIllegalAc.setStatus(_A)
swDlmsLicenseExpired=NotificationType((1,3,6,1,4,1,171,12,101,0,2))
swDlmsLicenseExpired.setObjects(*((_B,_D),(_B,_I)))
if mibBuilder.loadTexts:swDlmsLicenseExpired.setStatus(_A)
swDlmsLicenseInstallationSuccess=NotificationType((1,3,6,1,4,1,171,12,101,0,3))
swDlmsLicenseInstallationSuccess.setObjects(*((_B,_D),(_B,_G)))
if mibBuilder.loadTexts:swDlmsLicenseInstallationSuccess.setStatus(_A)
swDlmsLicenseExpiresIn30Days=NotificationType((1,3,6,1,4,1,171,12,101,0,4))
swDlmsLicenseExpiresIn30Days.setObjects(*((_B,_D),(_B,_G)))
if mibBuilder.loadTexts:swDlmsLicenseExpiresIn30Days.setStatus(_A)
swDlmsStackLicenseExpired=NotificationType((1,3,6,1,4,1,171,12,101,0,21))
swDlmsStackLicenseExpired.setObjects(*((_B,_E),(_B,_F),(_B,_J)))
if mibBuilder.loadTexts:swDlmsStackLicenseExpired.setStatus(_A)
swDlmsStackLicenseInstallationSuccess=NotificationType((1,3,6,1,4,1,171,12,101,0,22))
swDlmsStackLicenseInstallationSuccess.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:swDlmsStackLicenseInstallationSuccess.setStatus(_A)
swDlmsStackLicenseExpiresIn30Days=NotificationType((1,3,6,1,4,1,171,12,101,0,23))
swDlmsStackLicenseExpiresIn30Days.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:swDlmsStackLicenseExpiresIn30Days.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'swDlmsMIB':swDlmsMIB,'swDlmsNotifications':swDlmsNotifications,'swDlmsIllegalAc':swDlmsIllegalAc,'swDlmsLicenseExpired':swDlmsLicenseExpired,'swDlmsLicenseInstallationSuccess':swDlmsLicenseInstallationSuccess,'swDlmsLicenseExpiresIn30Days':swDlmsLicenseExpiresIn30Days,'swDlmsStackLicenseExpired':swDlmsStackLicenseExpired,'swDlmsStackLicenseInstallationSuccess':swDlmsStackLicenseInstallationSuccess,'swDlmsStackLicenseExpiresIn30Days':swDlmsStackLicenseExpiresIn30Days,'swDlmsObjects':swDlmsObjects,'swDlmsGeneralGroup':swDlmsGeneralGroup,_G:swDlmsInstallAc,'swDlmsInstallStackUnitId':swDlmsInstallStackUnitId,'swDlmsLicense':swDlmsLicense,'swDlmsLicenseModelTable':swDlmsLicenseModelTable,'swDlmsLicenseModelEntry':swDlmsLicenseModelEntry,_D:swDlmsLicenseModelName,'swDlmsLicenseModelRemaining':swDlmsLicenseModelRemaining,'swDlmsLicenseAcTable':swDlmsLicenseAcTable,'swDlmsLicenseAcEntry':swDlmsLicenseAcEntry,_I:swDlmsLicenseAc,'swDlmsLicenseAcStatus':swDlmsLicenseAcStatus,'swDlmsStackLicense':swDlmsStackLicense,'swDlmsStackLicenseModelTable':swDlmsStackLicenseModelTable,'swDlmsStackLicenseModelEntry':swDlmsStackLicenseModelEntry,_E:swDlmsStackLicenseModelUnitId,_F:swDlmsStackLicenseModelName,'swDlmsStackLicenseModelRemaining':swDlmsStackLicenseModelRemaining,'swDlmsStackLicenseAcTable':swDlmsStackLicenseAcTable,'swDlmsStackLicenseAcEntry':swDlmsStackLicenseAcEntry,_J:swDlmsStackLicenseAc,'swDlmsStackLicenseAcStatus':swDlmsStackLicenseAcStatus})