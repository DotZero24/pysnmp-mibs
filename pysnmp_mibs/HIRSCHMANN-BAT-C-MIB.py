_I='hmWLANVisibleAccessPointEntryIdx'
_H='hmComponentsIndex'
_G='HIRSCHMANN-BAT-C-MIB'
_F='IpAddress'
_E='OctetString'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,_F,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
hmModuleIdentity=ModuleIdentity((1,3,6,1,4,1,248,6))
if mibBuilder.loadTexts:hmModuleIdentity.setRevisions(('2012-05-09 00:00',))
class EnabledDisabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disableStatus',0),('enableStatus',1)))
_Hirschmann_ObjectIdentity=ObjectIdentity
hirschmann=_Hirschmann_ObjectIdentity((1,3,6,1,4,1,248))
_HmComponents_ObjectIdentity=ObjectIdentity
hmComponents=_HmComponents_ObjectIdentity((1,3,6,1,4,1,248,1))
_HmComponentsTable_Object=MibTable
hmComponentsTable=_HmComponentsTable_Object((1,3,6,1,4,1,248,1,1))
if mibBuilder.loadTexts:hmComponentsTable.setStatus(_A)
_HmComponentsEntry_Object=MibTableRow
hmComponentsEntry=_HmComponentsEntry_Object((1,3,6,1,4,1,248,1,1,1))
hmComponentsEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hmComponentsEntry.setStatus(_A)
class _HmComponentsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_HmComponentsIndex_Type.__name__=_C
_HmComponentsIndex_Object=MibTableColumn
hmComponentsIndex=_HmComponentsIndex_Object((1,3,6,1,4,1,248,1,1,1,1),_HmComponentsIndex_Type())
hmComponentsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hmComponentsIndex.setStatus(_A)
_HmComponentsName_Type=DisplayString
_HmComponentsName_Object=MibTableColumn
hmComponentsName=_HmComponentsName_Object((1,3,6,1,4,1,248,1,1,1,2),_HmComponentsName_Type())
hmComponentsName.setMaxAccess(_B)
if mibBuilder.loadTexts:hmComponentsName.setStatus(_A)
_HmComponentsDescr_Type=DisplayString
_HmComponentsDescr_Object=MibTableColumn
hmComponentsDescr=_HmComponentsDescr_Object((1,3,6,1,4,1,248,1,1,1,3),_HmComponentsDescr_Type())
hmComponentsDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:hmComponentsDescr.setStatus(_A)
_HmComponentsURL_Type=DisplayString
_HmComponentsURL_Object=MibTableColumn
hmComponentsURL=_HmComponentsURL_Object((1,3,6,1,4,1,248,1,1,1,4),_HmComponentsURL_Type())
hmComponentsURL.setMaxAccess(_B)
if mibBuilder.loadTexts:hmComponentsURL.setStatus(_A)
_HmComponentsOrderNumber_Type=DisplayString
_HmComponentsOrderNumber_Object=MibTableColumn
hmComponentsOrderNumber=_HmComponentsOrderNumber_Object((1,3,6,1,4,1,248,1,1,1,5),_HmComponentsOrderNumber_Type())
hmComponentsOrderNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hmComponentsOrderNumber.setStatus(_A)
_HmFirmware_ObjectIdentity=ObjectIdentity
hmFirmware=_HmFirmware_ObjectIdentity((1,3,6,1,4,1,248,2))
_HmFirmwareVersion_Type=DisplayString
_HmFirmwareVersion_Object=MibScalar
hmFirmwareVersion=_HmFirmwareVersion_Object((1,3,6,1,4,1,248,2,1),_HmFirmwareVersion_Type())
hmFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hmFirmwareVersion.setStatus(_A)
_HmFirmwareState_Type=DisplayString
_HmFirmwareState_Object=MibScalar
hmFirmwareState=_HmFirmwareState_Object((1,3,6,1,4,1,248,2,2),_HmFirmwareState_Type())
hmFirmwareState.setMaxAccess(_B)
if mibBuilder.loadTexts:hmFirmwareState.setStatus(_A)
_HmFirmwareDate_Type=DisplayString
_HmFirmwareDate_Object=MibScalar
hmFirmwareDate=_HmFirmwareDate_Object((1,3,6,1,4,1,248,2,3),_HmFirmwareDate_Type())
hmFirmwareDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hmFirmwareDate.setStatus(_A)
_HmFirmwareTime_Type=DisplayString
_HmFirmwareTime_Object=MibScalar
hmFirmwareTime=_HmFirmwareTime_Object((1,3,6,1,4,1,248,2,4),_HmFirmwareTime_Type())
hmFirmwareTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hmFirmwareTime.setStatus(_A)
_HmFirmwareCopyright_Type=DisplayString
_HmFirmwareCopyright_Object=MibScalar
hmFirmwareCopyright=_HmFirmwareCopyright_Object((1,3,6,1,4,1,248,2,5),_HmFirmwareCopyright_Type())
hmFirmwareCopyright.setMaxAccess(_B)
if mibBuilder.loadTexts:hmFirmwareCopyright.setStatus(_A)
_HmNet_ObjectIdentity=ObjectIdentity
hmNet=_HmNet_ObjectIdentity((1,3,6,1,4,1,248,3))
_HmNetPhyAddress_Type=MacAddress
_HmNetPhyAddress_Object=MibScalar
hmNetPhyAddress=_HmNetPhyAddress_Object((1,3,6,1,4,1,248,3,1),_HmNetPhyAddress_Type())
hmNetPhyAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hmNetPhyAddress.setStatus(_A)
class _HmNetIpAddress_Type(IpAddress):defaultHexValue='c0a80063'
_HmNetIpAddress_Type.__name__=_F
_HmNetIpAddress_Object=MibScalar
hmNetIpAddress=_HmNetIpAddress_Object((1,3,6,1,4,1,248,3,2),_HmNetIpAddress_Type())
hmNetIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hmNetIpAddress.setStatus(_A)
class _HmNetSubnetmask_Type(IpAddress):defaultHexValue='ffff0000'
_HmNetSubnetmask_Type.__name__=_F
_HmNetSubnetmask_Object=MibScalar
hmNetSubnetmask=_HmNetSubnetmask_Object((1,3,6,1,4,1,248,3,3),_HmNetSubnetmask_Type())
hmNetSubnetmask.setMaxAccess(_D)
if mibBuilder.loadTexts:hmNetSubnetmask.setStatus(_A)
class _HmNetGwIpAddress_Type(IpAddress):defaultHexValue='00000000'
_HmNetGwIpAddress_Type.__name__=_F
_HmNetGwIpAddress_Object=MibScalar
hmNetGwIpAddress=_HmNetGwIpAddress_Object((1,3,6,1,4,1,248,3,4),_HmNetGwIpAddress_Type())
hmNetGwIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hmNetGwIpAddress.setStatus(_A)
class _HmNetAssignment_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3)));namedValues=NamedValues(*(('other',0),('static',1),('dhcp',3)))
_HmNetAssignment_Type.__name__=_C
_HmNetAssignment_Object=MibScalar
hmNetAssignment=_HmNetAssignment_Object((1,3,6,1,4,1,248,3,7),_HmNetAssignment_Type())
hmNetAssignment.setMaxAccess(_D)
if mibBuilder.loadTexts:hmNetAssignment.setStatus(_A)
_HmWLAN_ObjectIdentity=ObjectIdentity
hmWLAN=_HmWLAN_ObjectIdentity((1,3,6,1,4,1,248,5))
_HmWLANParameter_ObjectIdentity=ObjectIdentity
hmWLANParameter=_HmWLANParameter_ObjectIdentity((1,3,6,1,4,1,248,5,1))
_HmWLANParameterState_Type=EnabledDisabledStatus
_HmWLANParameterState_Object=MibScalar
hmWLANParameterState=_HmWLANParameterState_Object((1,3,6,1,4,1,248,5,1,1),_HmWLANParameterState_Type())
hmWLANParameterState.setMaxAccess(_D)
if mibBuilder.loadTexts:hmWLANParameterState.setStatus(_A)
class _HmWLANParameterSSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HmWLANParameterSSID_Type.__name__=_E
_HmWLANParameterSSID_Object=MibScalar
hmWLANParameterSSID=_HmWLANParameterSSID_Object((1,3,6,1,4,1,248,5,1,3),_HmWLANParameterSSID_Type())
hmWLANParameterSSID.setMaxAccess(_D)
if mibBuilder.loadTexts:hmWLANParameterSSID.setStatus(_A)
class _HmWLANParameterMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('a',1),('b',2),('bg',3),('an',4),('gn',5),('bgn',6),('abgn',7)))
_HmWLANParameterMode_Type.__name__=_C
_HmWLANParameterMode_Object=MibScalar
hmWLANParameterMode=_HmWLANParameterMode_Object((1,3,6,1,4,1,248,5,1,4),_HmWLANParameterMode_Type())
hmWLANParameterMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWLANParameterMode.setStatus(_A)
class _HmWLANParameterChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HmWLANParameterChannel_Type.__name__=_C
_HmWLANParameterChannel_Object=MibScalar
hmWLANParameterChannel=_HmWLANParameterChannel_Object((1,3,6,1,4,1,248,5,1,5),_HmWLANParameterChannel_Type())
hmWLANParameterChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:hmWLANParameterChannel.setStatus(_A)
_HmWLANSecurity_ObjectIdentity=ObjectIdentity
hmWLANSecurity=_HmWLANSecurity_ObjectIdentity((1,3,6,1,4,1,248,5,2))
class _HmWLANSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('wpapsk',1),('wep64',2),('wep128',3)))
_HmWLANSecurityMode_Type.__name__=_C
_HmWLANSecurityMode_Object=MibScalar
hmWLANSecurityMode=_HmWLANSecurityMode_Object((1,3,6,1,4,1,248,5,2,1),_HmWLANSecurityMode_Type())
hmWLANSecurityMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hmWLANSecurityMode.setStatus(_A)
class _HmWLANSecurityWpaEncryptionAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('tkip',1),('aes',2),('both',3)))
_HmWLANSecurityWpaEncryptionAlgorithm_Type.__name__=_C
_HmWLANSecurityWpaEncryptionAlgorithm_Object=MibScalar
hmWLANSecurityWpaEncryptionAlgorithm=_HmWLANSecurityWpaEncryptionAlgorithm_Object((1,3,6,1,4,1,248,5,2,2),_HmWLANSecurityWpaEncryptionAlgorithm_Type())
hmWLANSecurityWpaEncryptionAlgorithm.setMaxAccess(_D)
if mibBuilder.loadTexts:hmWLANSecurityWpaEncryptionAlgorithm.setStatus(_A)
class _HmWLANSecurityWpaPsk_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_HmWLANSecurityWpaPsk_Type.__name__=_E
_HmWLANSecurityWpaPsk_Object=MibScalar
hmWLANSecurityWpaPsk=_HmWLANSecurityWpaPsk_Object((1,3,6,1,4,1,248,5,2,3),_HmWLANSecurityWpaPsk_Type())
hmWLANSecurityWpaPsk.setMaxAccess(_D)
if mibBuilder.loadTexts:hmWLANSecurityWpaPsk.setStatus(_A)
class _HmWLANSecurityWepAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('opensystem',0),('sharedkey',1),('wpawpa2psk',2)))
_HmWLANSecurityWepAuthType_Type.__name__=_C
_HmWLANSecurityWepAuthType_Object=MibScalar
hmWLANSecurityWepAuthType=_HmWLANSecurityWepAuthType_Object((1,3,6,1,4,1,248,5,2,4),_HmWLANSecurityWepAuthType_Type())
hmWLANSecurityWepAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:hmWLANSecurityWepAuthType.setStatus(_A)
class _HmWLANSecurityWepKeyEncoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('hex',0),('ascii',1)))
_HmWLANSecurityWepKeyEncoding_Type.__name__=_C
_HmWLANSecurityWepKeyEncoding_Object=MibScalar
hmWLANSecurityWepKeyEncoding=_HmWLANSecurityWepKeyEncoding_Object((1,3,6,1,4,1,248,5,2,5),_HmWLANSecurityWepKeyEncoding_Type())
hmWLANSecurityWepKeyEncoding.setMaxAccess(_D)
if mibBuilder.loadTexts:hmWLANSecurityWepKeyEncoding.setStatus(_A)
class _HmWLANSecurityWepKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,26))
_HmWLANSecurityWepKey_Type.__name__=_E
_HmWLANSecurityWepKey_Object=MibScalar
hmWLANSecurityWepKey=_HmWLANSecurityWepKey_Object((1,3,6,1,4,1,248,5,2,6),_HmWLANSecurityWepKey_Type())
hmWLANSecurityWepKey.setMaxAccess(_D)
if mibBuilder.loadTexts:hmWLANSecurityWepKey.setStatus(_A)
_HmWLANVisibleAccessPointTable_Object=MibTable
hmWLANVisibleAccessPointTable=_HmWLANVisibleAccessPointTable_Object((1,3,6,1,4,1,248,5,3))
if mibBuilder.loadTexts:hmWLANVisibleAccessPointTable.setStatus(_A)
_HmWLANVisibleAccessPointEntry_Object=MibTableRow
hmWLANVisibleAccessPointEntry=_HmWLANVisibleAccessPointEntry_Object((1,3,6,1,4,1,248,5,3,1))
hmWLANVisibleAccessPointEntry.setIndexNames((0,_G,_I))
if mibBuilder.loadTexts:hmWLANVisibleAccessPointEntry.setStatus(_A)
class _HmWLANVisibleAccessPointEntryIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,49))
_HmWLANVisibleAccessPointEntryIdx_Type.__name__=_C
_HmWLANVisibleAccessPointEntryIdx_Object=MibTableColumn
hmWLANVisibleAccessPointEntryIdx=_HmWLANVisibleAccessPointEntryIdx_Object((1,3,6,1,4,1,248,5,3,1,1),_HmWLANVisibleAccessPointEntryIdx_Type())
hmWLANVisibleAccessPointEntryIdx.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hmWLANVisibleAccessPointEntryIdx.setStatus(_A)
_HmWLANVisibleAccessPointEntrySNR_Type=Integer32
_HmWLANVisibleAccessPointEntrySNR_Object=MibTableColumn
hmWLANVisibleAccessPointEntrySNR=_HmWLANVisibleAccessPointEntrySNR_Object((1,3,6,1,4,1,248,5,3,1,2),_HmWLANVisibleAccessPointEntrySNR_Type())
hmWLANVisibleAccessPointEntrySNR.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWLANVisibleAccessPointEntrySNR.setStatus(_A)
class _HmWLANVisibleAccessPointEntryChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HmWLANVisibleAccessPointEntryChannel_Type.__name__=_C
_HmWLANVisibleAccessPointEntryChannel_Object=MibTableColumn
hmWLANVisibleAccessPointEntryChannel=_HmWLANVisibleAccessPointEntryChannel_Object((1,3,6,1,4,1,248,5,3,1,3),_HmWLANVisibleAccessPointEntryChannel_Type())
hmWLANVisibleAccessPointEntryChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWLANVisibleAccessPointEntryChannel.setStatus(_A)
class _HmWLANVisibleAccessPointEntryPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HmWLANVisibleAccessPointEntryPower_Type.__name__=_C
_HmWLANVisibleAccessPointEntryPower_Object=MibTableColumn
hmWLANVisibleAccessPointEntryPower=_HmWLANVisibleAccessPointEntryPower_Object((1,3,6,1,4,1,248,5,3,1,4),_HmWLANVisibleAccessPointEntryPower_Type())
hmWLANVisibleAccessPointEntryPower.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWLANVisibleAccessPointEntryPower.setStatus(_A)
_HmWLANVisibleAccessPointEntrySSID_Type=OctetString
_HmWLANVisibleAccessPointEntrySSID_Object=MibTableColumn
hmWLANVisibleAccessPointEntrySSID=_HmWLANVisibleAccessPointEntrySSID_Object((1,3,6,1,4,1,248,5,3,1,5),_HmWLANVisibleAccessPointEntrySSID_Type())
hmWLANVisibleAccessPointEntrySSID.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWLANVisibleAccessPointEntrySSID.setStatus(_A)
_HmWLANVisibleAccessPointEntrySecurity_Type=OctetString
_HmWLANVisibleAccessPointEntrySecurity_Object=MibTableColumn
hmWLANVisibleAccessPointEntrySecurity=_HmWLANVisibleAccessPointEntrySecurity_Object((1,3,6,1,4,1,248,5,3,1,6),_HmWLANVisibleAccessPointEntrySecurity_Type())
hmWLANVisibleAccessPointEntrySecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWLANVisibleAccessPointEntrySecurity.setStatus(_A)
_HmWLANVisibleAccessPointEntryAddress_Type=MacAddress
_HmWLANVisibleAccessPointEntryAddress_Object=MibTableColumn
hmWLANVisibleAccessPointEntryAddress=_HmWLANVisibleAccessPointEntryAddress_Object((1,3,6,1,4,1,248,5,3,1,7),_HmWLANVisibleAccessPointEntryAddress_Type())
hmWLANVisibleAccessPointEntryAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWLANVisibleAccessPointEntryAddress.setStatus(_A)
class _HmWLANVisibleAccessPointEntryConnected_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_HmWLANVisibleAccessPointEntryConnected_Type.__name__=_C
_HmWLANVisibleAccessPointEntryConnected_Object=MibTableColumn
hmWLANVisibleAccessPointEntryConnected=_HmWLANVisibleAccessPointEntryConnected_Object((1,3,6,1,4,1,248,5,3,1,8),_HmWLANVisibleAccessPointEntryConnected_Type())
hmWLANVisibleAccessPointEntryConnected.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWLANVisibleAccessPointEntryConnected.setStatus(_A)
_HmWLANVisibleAccessPointEntryRSSI_Type=Integer32
_HmWLANVisibleAccessPointEntryRSSI_Object=MibTableColumn
hmWLANVisibleAccessPointEntryRSSI=_HmWLANVisibleAccessPointEntryRSSI_Object((1,3,6,1,4,1,248,5,3,1,9),_HmWLANVisibleAccessPointEntryRSSI_Type())
hmWLANVisibleAccessPointEntryRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWLANVisibleAccessPointEntryRSSI.setStatus(_A)
_HmWLANVisibleAccessPointEntryNoise_Type=Integer32
_HmWLANVisibleAccessPointEntryNoise_Object=MibTableColumn
hmWLANVisibleAccessPointEntryNoise=_HmWLANVisibleAccessPointEntryNoise_Object((1,3,6,1,4,1,248,5,3,1,10),_HmWLANVisibleAccessPointEntryNoise_Type())
hmWLANVisibleAccessPointEntryNoise.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWLANVisibleAccessPointEntryNoise.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'EnabledDisabledStatus':EnabledDisabledStatus,'hirschmann':hirschmann,'hmComponents':hmComponents,'hmComponentsTable':hmComponentsTable,'hmComponentsEntry':hmComponentsEntry,_H:hmComponentsIndex,'hmComponentsName':hmComponentsName,'hmComponentsDescr':hmComponentsDescr,'hmComponentsURL':hmComponentsURL,'hmComponentsOrderNumber':hmComponentsOrderNumber,'hmFirmware':hmFirmware,'hmFirmwareVersion':hmFirmwareVersion,'hmFirmwareState':hmFirmwareState,'hmFirmwareDate':hmFirmwareDate,'hmFirmwareTime':hmFirmwareTime,'hmFirmwareCopyright':hmFirmwareCopyright,'hmNet':hmNet,'hmNetPhyAddress':hmNetPhyAddress,'hmNetIpAddress':hmNetIpAddress,'hmNetSubnetmask':hmNetSubnetmask,'hmNetGwIpAddress':hmNetGwIpAddress,'hmNetAssignment':hmNetAssignment,'hmWLAN':hmWLAN,'hmWLANParameter':hmWLANParameter,'hmWLANParameterState':hmWLANParameterState,'hmWLANParameterSSID':hmWLANParameterSSID,'hmWLANParameterMode':hmWLANParameterMode,'hmWLANParameterChannel':hmWLANParameterChannel,'hmWLANSecurity':hmWLANSecurity,'hmWLANSecurityMode':hmWLANSecurityMode,'hmWLANSecurityWpaEncryptionAlgorithm':hmWLANSecurityWpaEncryptionAlgorithm,'hmWLANSecurityWpaPsk':hmWLANSecurityWpaPsk,'hmWLANSecurityWepAuthType':hmWLANSecurityWepAuthType,'hmWLANSecurityWepKeyEncoding':hmWLANSecurityWepKeyEncoding,'hmWLANSecurityWepKey':hmWLANSecurityWepKey,'hmWLANVisibleAccessPointTable':hmWLANVisibleAccessPointTable,'hmWLANVisibleAccessPointEntry':hmWLANVisibleAccessPointEntry,_I:hmWLANVisibleAccessPointEntryIdx,'hmWLANVisibleAccessPointEntrySNR':hmWLANVisibleAccessPointEntrySNR,'hmWLANVisibleAccessPointEntryChannel':hmWLANVisibleAccessPointEntryChannel,'hmWLANVisibleAccessPointEntryPower':hmWLANVisibleAccessPointEntryPower,'hmWLANVisibleAccessPointEntrySSID':hmWLANVisibleAccessPointEntrySSID,'hmWLANVisibleAccessPointEntrySecurity':hmWLANVisibleAccessPointEntrySecurity,'hmWLANVisibleAccessPointEntryAddress':hmWLANVisibleAccessPointEntryAddress,'hmWLANVisibleAccessPointEntryConnected':hmWLANVisibleAccessPointEntryConnected,'hmWLANVisibleAccessPointEntryRSSI':hmWLANVisibleAccessPointEntryRSSI,'hmWLANVisibleAccessPointEntryNoise':hmWLANVisibleAccessPointEntryNoise,'hmModuleIdentity':hmModuleIdentity})