_E='ArrisMocaTabooChannelMsk'
_D='ArrisMocaChannelMsk'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
arrisProducts,=mibBuilder.importSymbols('ARRIS-MIB','arrisProducts')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
arrisMoCAMib=ModuleIdentity((1,3,6,1,4,1,4115,1,21))
if mibBuilder.loadTexts:arrisMoCAMib.setRevisions(('2014-08-13 00:00','2013-08-21 00:00','2013-08-01 00:00','2013-06-26 00:00','2013-06-04 00:00','2012-11-18 00:00','2012-11-04 00:00','2012-10-10 00:00'))
class ArrisMocaTabooChannelMsk(TextualConvention,Unsigned32):status=_A
class ArrisMocaChannelMsk(TextualConvention,Unsigned32):status=_A
_ArrisMoCAConfiguration_ObjectIdentity=ObjectIdentity
arrisMoCAConfiguration=_ArrisMoCAConfiguration_ObjectIdentity((1,3,6,1,4,1,4115,1,21,1))
class _ArrisMoCAChannelSelMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('scan',1),('manual',2)))
_ArrisMoCAChannelSelMethod_Type.__name__=_C
_ArrisMoCAChannelSelMethod_Object=MibScalar
arrisMoCAChannelSelMethod=_ArrisMoCAChannelSelMethod_Object((1,3,6,1,4,1,4115,1,21,1,1),_ArrisMoCAChannelSelMethod_Type())
arrisMoCAChannelSelMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisMoCAChannelSelMethod.setStatus(_A)
class _ArrisMoCAChannelMsk_Type(ArrisMocaChannelMsk):defaultValue=1
_ArrisMoCAChannelMsk_Type.__name__=_D
_ArrisMoCAChannelMsk_Object=MibScalar
arrisMoCAChannelMsk=_ArrisMoCAChannelMsk_Object((1,3,6,1,4,1,4115,1,21,1,2),_ArrisMoCAChannelMsk_Type())
arrisMoCAChannelMsk.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisMoCAChannelMsk.setStatus(_A)
class _ArrisMoCATabooChannel_Type(ArrisMocaTabooChannelMsk):defaultValue=0
_ArrisMoCATabooChannel_Type.__name__=_E
_ArrisMoCATabooChannel_Object=MibScalar
arrisMoCATabooChannel=_ArrisMoCATabooChannel_Object((1,3,6,1,4,1,4115,1,21,1,4),_ArrisMoCATabooChannel_Type())
arrisMoCATabooChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisMoCATabooChannel.setStatus(_A)
class _ArrisMoCALOF_Type(Integer32):defaultValue=1150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1150,1200,1250,1300,1350,1400,1450,1500,1550,1600)));namedValues=NamedValues(*(('d1',1150),('d2',1200),('d3',1250),('d4',1300),('d5',1350),('d6',1400),('d7',1450),('d8',1500),('d9',1550),('d10',1600)))
_ArrisMoCALOF_Type.__name__=_C
_ArrisMoCALOF_Object=MibScalar
arrisMoCALOF=_ArrisMoCALOF_Object((1,3,6,1,4,1,4115,1,21,1,5),_ArrisMoCALOF_Type())
arrisMoCALOF.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisMoCALOF.setStatus(_A)
class _ArrisMoCAPrimchnOff_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('same',0),('above',1),('below',2)))
_ArrisMoCAPrimchnOff_Type.__name__=_C
_ArrisMoCAPrimchnOff_Object=MibScalar
arrisMoCAPrimchnOff=_ArrisMoCAPrimchnOff_Object((1,3,6,1,4,1,4115,1,21,1,6),_ArrisMoCAPrimchnOff_Type())
arrisMoCAPrimchnOff.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisMoCAPrimchnOff.setStatus(_A)
class _ArrisMoCAApplySettings_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unknown',0),('applySettings-Save',1),('applySettings-NoSave',2)))
_ArrisMoCAApplySettings_Type.__name__=_C
_ArrisMoCAApplySettings_Object=MibScalar
arrisMoCAApplySettings=_ArrisMoCAApplySettings_Object((1,3,6,1,4,1,4115,1,21,2),_ArrisMoCAApplySettings_Type())
arrisMoCAApplySettings.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisMoCAApplySettings.setStatus(_A)
mibBuilder.exportSymbols('ARRIS-MOCA-MIB',**{_E:ArrisMocaTabooChannelMsk,_D:ArrisMocaChannelMsk,'arrisMoCAMib':arrisMoCAMib,'arrisMoCAConfiguration':arrisMoCAConfiguration,'arrisMoCAChannelSelMethod':arrisMoCAChannelSelMethod,'arrisMoCAChannelMsk':arrisMoCAChannelMsk,'arrisMoCATabooChannel':arrisMoCATabooChannel,'arrisMoCALOF':arrisMoCALOF,'arrisMoCAPrimchnOff':arrisMoCAPrimchnOff,'arrisMoCAApplySettings':arrisMoCAApplySettings})