_E='read-only'
_D='DisplayString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('DLINK-3100-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention','TruthValue')
rlCli=ModuleIdentity((1,3,6,1,4,1,171,10,94,89,89,52))
if mibBuilder.loadTexts:rlCli.setRevisions(('2007-01-02 00:00',))
_RlCliMibVersion_Type=Integer32
_RlCliMibVersion_Object=MibScalar
rlCliMibVersion=_RlCliMibVersion_Object((1,3,6,1,4,1,171,10,94,89,89,52,1),_RlCliMibVersion_Type())
rlCliMibVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:rlCliMibVersion.setStatus(_A)
class _RlCliPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RlCliPassword_Type.__name__=_D
_RlCliPassword_Object=MibScalar
rlCliPassword=_RlCliPassword_Object((1,3,6,1,4,1,171,10,94,89,89,52,2),_RlCliPassword_Type())
rlCliPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCliPassword.setStatus(_A)
class _RlCliTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,3600))
_RlCliTimer_Type.__name__=_C
_RlCliTimer_Object=MibScalar
rlCliTimer=_RlCliTimer_Object((1,3,6,1,4,1,171,10,94,89,89,52,3),_RlCliTimer_Type())
rlCliTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCliTimer.setStatus(_A)
_RlCliFileEnable_Type=TruthValue
_RlCliFileEnable_Object=MibScalar
rlCliFileEnable=_RlCliFileEnable_Object((1,3,6,1,4,1,171,10,94,89,89,52,4),_RlCliFileEnable_Type())
rlCliFileEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rlCliFileEnable.setStatus(_A)
_RlCliFileEnableAfterReset_Type=TruthValue
_RlCliFileEnableAfterReset_Object=MibScalar
rlCliFileEnableAfterReset=_RlCliFileEnableAfterReset_Object((1,3,6,1,4,1,171,10,94,89,89,52,5),_RlCliFileEnableAfterReset_Type())
rlCliFileEnableAfterReset.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCliFileEnableAfterReset.setStatus(_A)
mibBuilder.exportSymbols('DLINK-3100-CLI-MIB',**{'rlCli':rlCli,'rlCliMibVersion':rlCliMibVersion,'rlCliPassword':rlCliPassword,'rlCliTimer':rlCliTimer,'rlCliFileEnable':rlCliFileEnable,'rlCliFileEnableAfterReset':rlCliFileEnableAfterReset})