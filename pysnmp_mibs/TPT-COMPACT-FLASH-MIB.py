_F='tptCompactFlashDeviceStatus'
_E='tptCompactFlashDeviceID'
_D='TPT-COMPACT-FLASH-MIB'
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
tpt_tpa_eventsV2,tpt_tpa_objs,tpt_tpa_unkparams=mibBuilder.importSymbols('TPT-TPAMIBS-MIB','tpt-tpa-eventsV2','tpt-tpa-objs','tpt-tpa-unkparams')
tpt_compact_flash=ModuleIdentity((1,3,6,1,4,1,10734,3,3,2,14))
if mibBuilder.loadTexts:tpt_compact_flash.setRevisions(('2016-05-25 18:54',))
class MountedOrNot(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('mounted',0),('unmounted',1)))
class OperationMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('secure',0),('auto-mount',1)))
class FormattedOrNot(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('formatted',0),('unformatted',1)))
class PresentOrNot(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('present',0),('absent',1)))
_CompactFlashPresent_Type=PresentOrNot
_CompactFlashPresent_Object=MibScalar
compactFlashPresent=_CompactFlashPresent_Object((1,3,6,1,4,1,10734,3,3,2,14,1),_CompactFlashPresent_Type())
compactFlashPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:compactFlashPresent.setStatus(_A)
_CompactFlashMounted_Type=MountedOrNot
_CompactFlashMounted_Object=MibScalar
compactFlashMounted=_CompactFlashMounted_Object((1,3,6,1,4,1,10734,3,3,2,14,2),_CompactFlashMounted_Type())
compactFlashMounted.setMaxAccess(_B)
if mibBuilder.loadTexts:compactFlashMounted.setStatus(_A)
_CompactFlashFormatted_Type=FormattedOrNot
_CompactFlashFormatted_Object=MibScalar
compactFlashFormatted=_CompactFlashFormatted_Object((1,3,6,1,4,1,10734,3,3,2,14,3),_CompactFlashFormatted_Type())
compactFlashFormatted.setMaxAccess(_B)
if mibBuilder.loadTexts:compactFlashFormatted.setStatus(_A)
_CompactFlashOperationMode_Type=OperationMode
_CompactFlashOperationMode_Object=MibScalar
compactFlashOperationMode=_CompactFlashOperationMode_Object((1,3,6,1,4,1,10734,3,3,2,14,4),_CompactFlashOperationMode_Type())
compactFlashOperationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:compactFlashOperationMode.setStatus(_A)
_VendorInformation_ObjectIdentity=ObjectIdentity
vendorInformation=_VendorInformation_ObjectIdentity((1,3,6,1,4,1,10734,3,3,2,14,5))
if mibBuilder.loadTexts:vendorInformation.setStatus(_A)
class _SerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SerialNumber_Type.__name__=_C
_SerialNumber_Object=MibScalar
serialNumber=_SerialNumber_Object((1,3,6,1,4,1,10734,3,3,2,14,5,1),_SerialNumber_Type())
serialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:serialNumber.setStatus(_A)
class _Model_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_Model_Type.__name__=_C
_Model_Object=MibScalar
model=_Model_Object((1,3,6,1,4,1,10734,3,3,2,14,5,2),_Model_Type())
model.setMaxAccess(_B)
if mibBuilder.loadTexts:model.setStatus(_A)
_Capacity_Type=Unsigned32
_Capacity_Object=MibScalar
capacity=_Capacity_Object((1,3,6,1,4,1,10734,3,3,2,14,5,3),_Capacity_Type())
capacity.setMaxAccess(_B)
if mibBuilder.loadTexts:capacity.setStatus(_A)
class _Revision_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_Revision_Type.__name__=_C
_Revision_Object=MibScalar
revision=_Revision_Object((1,3,6,1,4,1,10734,3,3,2,14,5,4),_Revision_Type())
revision.setMaxAccess(_B)
if mibBuilder.loadTexts:revision.setStatus(_A)
class _TptCompactFlashDeviceID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TptCompactFlashDeviceID_Type.__name__=_C
_TptCompactFlashDeviceID_Object=MibScalar
tptCompactFlashDeviceID=_TptCompactFlashDeviceID_Object((1,3,6,1,4,1,10734,3,3,3,1,261),_TptCompactFlashDeviceID_Type())
tptCompactFlashDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:tptCompactFlashDeviceID.setStatus(_A)
_TptCompactFlashDeviceStatus_Type=PresentOrNot
_TptCompactFlashDeviceStatus_Object=MibScalar
tptCompactFlashDeviceStatus=_TptCompactFlashDeviceStatus_Object((1,3,6,1,4,1,10734,3,3,3,1,262),_TptCompactFlashDeviceStatus_Type())
tptCompactFlashDeviceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tptCompactFlashDeviceStatus.setStatus(_A)
tptCFInsertedNotify=NotificationType((1,3,6,1,4,1,10734,3,3,3,0,51))
tptCFInsertedNotify.setObjects(*((_D,_E),(_D,_F)))
if mibBuilder.loadTexts:tptCFInsertedNotify.setStatus(_A)
tptCFEjectedNotify=NotificationType((1,3,6,1,4,1,10734,3,3,3,0,52))
tptCFEjectedNotify.setObjects(*((_D,_E),(_D,_F)))
if mibBuilder.loadTexts:tptCFEjectedNotify.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'MountedOrNot':MountedOrNot,'OperationMode':OperationMode,'FormattedOrNot':FormattedOrNot,'PresentOrNot':PresentOrNot,'tpt-compact-flash':tpt_compact_flash,'compactFlashPresent':compactFlashPresent,'compactFlashMounted':compactFlashMounted,'compactFlashFormatted':compactFlashFormatted,'compactFlashOperationMode':compactFlashOperationMode,'vendorInformation':vendorInformation,'serialNumber':serialNumber,'model':model,'capacity':capacity,'revision':revision,'tptCFInsertedNotify':tptCFInsertedNotify,'tptCFEjectedNotify':tptCFEjectedNotify,_E:tptCompactFlashDeviceID,_F:tptCompactFlashDeviceStatus})