_D='Unsigned32'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fseoam=ModuleIdentity((1,3,6,1,4,1,10876,101,1,121))
if mibBuilder.loadTexts:fseoam.setRevisions(('2012-09-05 00:00',))
class EoamOui(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_FsEoamSystem_ObjectIdentity=ObjectIdentity
fsEoamSystem=_FsEoamSystem_ObjectIdentity((1,3,6,1,4,1,10876,101,1,121,1))
class _FsEoamSystemControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_FsEoamSystemControl_Type.__name__=_C
_FsEoamSystemControl_Object=MibScalar
fsEoamSystemControl=_FsEoamSystemControl_Object((1,3,6,1,4,1,10876,101,1,121,1,1),_FsEoamSystemControl_Type())
fsEoamSystemControl.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEoamSystemControl.setStatus(_A)
class _FsEoamModuleStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_FsEoamModuleStatus_Type.__name__=_C
_FsEoamModuleStatus_Object=MibScalar
fsEoamModuleStatus=_FsEoamModuleStatus_Object((1,3,6,1,4,1,10876,101,1,121,1,2),_FsEoamModuleStatus_Type())
fsEoamModuleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEoamModuleStatus.setStatus(_A)
class _FsEoamErrorEventResend_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FsEoamErrorEventResend_Type.__name__=_D
_FsEoamErrorEventResend_Object=MibScalar
fsEoamErrorEventResend=_FsEoamErrorEventResend_Object((1,3,6,1,4,1,10876,101,1,121,1,3),_FsEoamErrorEventResend_Type())
fsEoamErrorEventResend.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEoamErrorEventResend.setStatus(_A)
_FsEoamOui_Type=EoamOui
_FsEoamOui_Object=MibScalar
fsEoamOui=_FsEoamOui_Object((1,3,6,1,4,1,10876,101,1,121,1,4),_FsEoamOui_Type())
fsEoamOui.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEoamOui.setStatus(_A)
class _FsEoamTraceOption_Type(Integer32):defaultValue=262144
_FsEoamTraceOption_Type.__name__=_C
_FsEoamTraceOption_Object=MibScalar
fsEoamTraceOption=_FsEoamTraceOption_Object((1,3,6,1,4,1,10876,101,1,121,1,5),_FsEoamTraceOption_Type())
fsEoamTraceOption.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEoamTraceOption.setStatus(_A)
mibBuilder.exportSymbols('EOAM-MIB',**{'EoamOui':EoamOui,'fseoam':fseoam,'fsEoamSystem':fsEoamSystem,'fsEoamSystemControl':fsEoamSystemControl,'fsEoamModuleStatus':fsEoamModuleStatus,'fsEoamErrorEventResend':fsEoamErrorEventResend,'fsEoamOui':fsEoamOui,'fsEoamTraceOption':fsEoamTraceOption})