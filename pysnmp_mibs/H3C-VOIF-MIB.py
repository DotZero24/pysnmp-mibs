_J='disable'
_I='enable'
_H='not-accessible'
_G='h3cVoIfCfgGroupNumber'
_F='h3cVoIfCfgPortNumber'
_E='OctetString'
_D='H3C-VOIF-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cVoice,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cVoice')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cVoiceIf=ModuleIdentity((1,3,6,1,4,1,2011,10,2,39,2))
if mibBuilder.loadTexts:h3cVoiceIf.setRevisions(('2005-03-15 00:00',))
_H3cVoIfObjects_ObjectIdentity=ObjectIdentity
h3cVoIfObjects=_H3cVoIfObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,39,2,1))
_H3cVoIfConfigTable_Object=MibTable
h3cVoIfConfigTable=_H3cVoIfConfigTable_Object((1,3,6,1,4,1,2011,10,2,39,2,1,1))
if mibBuilder.loadTexts:h3cVoIfConfigTable.setStatus(_A)
_H3cVoIfConfigEntry_Object=MibTableRow
h3cVoIfConfigEntry=_H3cVoIfConfigEntry_Object((1,3,6,1,4,1,2011,10,2,39,2,1,1,1))
h3cVoIfConfigEntry.setIndexNames((0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:h3cVoIfConfigEntry.setStatus(_A)
_H3cVoIfCfgPortNumber_Type=Integer32
_H3cVoIfCfgPortNumber_Object=MibTableColumn
h3cVoIfCfgPortNumber=_H3cVoIfCfgPortNumber_Object((1,3,6,1,4,1,2011,10,2,39,2,1,1,1,1),_H3cVoIfCfgPortNumber_Type())
h3cVoIfCfgPortNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cVoIfCfgPortNumber.setStatus(_A)
_H3cVoIfCfgGroupNumber_Type=Integer32
_H3cVoIfCfgGroupNumber_Object=MibTableColumn
h3cVoIfCfgGroupNumber=_H3cVoIfCfgGroupNumber_Object((1,3,6,1,4,1,2011,10,2,39,2,1,1,1,2),_H3cVoIfCfgGroupNumber_Type())
h3cVoIfCfgGroupNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cVoIfCfgGroupNumber.setStatus(_A)
class _H3cVoIfCfgCngOn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_H3cVoIfCfgCngOn_Type.__name__=_C
_H3cVoIfCfgCngOn_Object=MibTableColumn
h3cVoIfCfgCngOn=_H3cVoIfCfgCngOn_Object((1,3,6,1,4,1,2011,10,2,39,2,1,1,1,3),_H3cVoIfCfgCngOn_Type())
h3cVoIfCfgCngOn.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoIfCfgCngOn.setStatus(_A)
_H3cVoIfConfigInputGain_Type=Integer32
_H3cVoIfConfigInputGain_Object=MibTableColumn
h3cVoIfConfigInputGain=_H3cVoIfConfigInputGain_Object((1,3,6,1,4,1,2011,10,2,39,2,1,1,1,4),_H3cVoIfConfigInputGain_Type())
h3cVoIfConfigInputGain.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoIfConfigInputGain.setStatus(_A)
class _H3cVoIfConfigOutputGain_Type(Integer32):defaultValue=0
_H3cVoIfConfigOutputGain_Type.__name__=_C
_H3cVoIfConfigOutputGain_Object=MibTableColumn
h3cVoIfConfigOutputGain=_H3cVoIfConfigOutputGain_Object((1,3,6,1,4,1,2011,10,2,39,2,1,1,1,5),_H3cVoIfConfigOutputGain_Type())
h3cVoIfConfigOutputGain.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoIfConfigOutputGain.setStatus(_A)
class _H3cVoIfCfgEchoCancelSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_H3cVoIfCfgEchoCancelSwitch_Type.__name__=_C
_H3cVoIfCfgEchoCancelSwitch_Object=MibTableColumn
h3cVoIfCfgEchoCancelSwitch=_H3cVoIfCfgEchoCancelSwitch_Object((1,3,6,1,4,1,2011,10,2,39,2,1,1,1,6),_H3cVoIfCfgEchoCancelSwitch_Type())
h3cVoIfCfgEchoCancelSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoIfCfgEchoCancelSwitch.setStatus(_A)
_H3cVoIfCfgEchoCancellDelay_Type=Integer32
_H3cVoIfCfgEchoCancellDelay_Object=MibTableColumn
h3cVoIfCfgEchoCancellDelay=_H3cVoIfCfgEchoCancellDelay_Object((1,3,6,1,4,1,2011,10,2,39,2,1,1,1,7),_H3cVoIfCfgEchoCancellDelay_Type())
h3cVoIfCfgEchoCancellDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoIfCfgEchoCancellDelay.setStatus(_A)
class _H3cVoIfCfgPlarNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_H3cVoIfCfgPlarNumber_Type.__name__=_E
_H3cVoIfCfgPlarNumber_Object=MibTableColumn
h3cVoIfCfgPlarNumber=_H3cVoIfCfgPlarNumber_Object((1,3,6,1,4,1,2011,10,2,39,2,1,1,1,8),_H3cVoIfCfgPlarNumber_Type())
h3cVoIfCfgPlarNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoIfCfgPlarNumber.setStatus(_A)
_H3cVoIfCfgDescription_Type=OctetString
_H3cVoIfCfgDescription_Object=MibTableColumn
h3cVoIfCfgDescription=_H3cVoIfCfgDescription_Object((1,3,6,1,4,1,2011,10,2,39,2,1,1,1,9),_H3cVoIfCfgDescription_Type())
h3cVoIfCfgDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoIfCfgDescription.setStatus(_A)
class _H3cVoIfCfgStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_H3cVoIfCfgStatus_Type.__name__=_C
_H3cVoIfCfgStatus_Object=MibTableColumn
h3cVoIfCfgStatus=_H3cVoIfCfgStatus_Object((1,3,6,1,4,1,2011,10,2,39,2,1,1,1,10),_H3cVoIfCfgStatus_Type())
h3cVoIfCfgStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoIfCfgStatus.setStatus(_A)
class _H3cVoIfCfgCallingNumSubstRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cVoIfCfgCallingNumSubstRule_Type.__name__=_C
_H3cVoIfCfgCallingNumSubstRule_Object=MibTableColumn
h3cVoIfCfgCallingNumSubstRule=_H3cVoIfCfgCallingNumSubstRule_Object((1,3,6,1,4,1,2011,10,2,39,2,1,1,1,11),_H3cVoIfCfgCallingNumSubstRule_Type())
h3cVoIfCfgCallingNumSubstRule.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoIfCfgCallingNumSubstRule.setStatus(_A)
class _H3cVoIfCfgCalledNumSubstRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cVoIfCfgCalledNumSubstRule_Type.__name__=_C
_H3cVoIfCfgCalledNumSubstRule_Object=MibTableColumn
h3cVoIfCfgCalledNumSubstRule=_H3cVoIfCfgCalledNumSubstRule_Object((1,3,6,1,4,1,2011,10,2,39,2,1,1,1,12),_H3cVoIfCfgCalledNumSubstRule_Type())
h3cVoIfCfgCalledNumSubstRule.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoIfCfgCalledNumSubstRule.setStatus(_A)
_H3cVoIfCfgSubLine_Type=OctetString
_H3cVoIfCfgSubLine_Object=MibTableColumn
h3cVoIfCfgSubLine=_H3cVoIfCfgSubLine_Object((1,3,6,1,4,1,2011,10,2,39,2,1,1,1,13),_H3cVoIfCfgSubLine_Type())
h3cVoIfCfgSubLine.setMaxAccess('read-only')
if mibBuilder.loadTexts:h3cVoIfCfgSubLine.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'h3cVoiceIf':h3cVoiceIf,'h3cVoIfObjects':h3cVoIfObjects,'h3cVoIfConfigTable':h3cVoIfConfigTable,'h3cVoIfConfigEntry':h3cVoIfConfigEntry,_F:h3cVoIfCfgPortNumber,_G:h3cVoIfCfgGroupNumber,'h3cVoIfCfgCngOn':h3cVoIfCfgCngOn,'h3cVoIfConfigInputGain':h3cVoIfConfigInputGain,'h3cVoIfConfigOutputGain':h3cVoIfConfigOutputGain,'h3cVoIfCfgEchoCancelSwitch':h3cVoIfCfgEchoCancelSwitch,'h3cVoIfCfgEchoCancellDelay':h3cVoIfCfgEchoCancellDelay,'h3cVoIfCfgPlarNumber':h3cVoIfCfgPlarNumber,'h3cVoIfCfgDescription':h3cVoIfCfgDescription,'h3cVoIfCfgStatus':h3cVoIfCfgStatus,'h3cVoIfCfgCallingNumSubstRule':h3cVoIfCfgCallingNumSubstRule,'h3cVoIfCfgCalledNumSubstRule':h3cVoIfCfgCalledNumSubstRule,'h3cVoIfCfgSubLine':h3cVoIfCfgSubLine})