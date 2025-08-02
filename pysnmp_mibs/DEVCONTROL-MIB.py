_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
device,=mibBuilder.importSymbols('ANIROOT-MIB','device')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
aniDevControl=ModuleIdentity((1,3,6,1,4,1,4325,2,4))
_AniDevControlResetDevice_Type=TruthValue
_AniDevControlResetDevice_Object=MibScalar
aniDevControlResetDevice=_AniDevControlResetDevice_Object((1,3,6,1,4,1,4325,2,4,1),_AniDevControlResetDevice_Type())
aniDevControlResetDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:aniDevControlResetDevice.setStatus(_A)
_AniDevControlSetFactoryDefaults_Type=TruthValue
_AniDevControlSetFactoryDefaults_Object=MibScalar
aniDevControlSetFactoryDefaults=_AniDevControlSetFactoryDefaults_Object((1,3,6,1,4,1,4325,2,4,2),_AniDevControlSetFactoryDefaults_Type())
aniDevControlSetFactoryDefaults.setMaxAccess(_D)
if mibBuilder.loadTexts:aniDevControlSetFactoryDefaults.setStatus(_A)
_AniDevControlStartUpload_Type=TruthValue
_AniDevControlStartUpload_Object=MibScalar
aniDevControlStartUpload=_AniDevControlStartUpload_Object((1,3,6,1,4,1,4325,2,4,3),_AniDevControlStartUpload_Type())
aniDevControlStartUpload.setMaxAccess(_C)
if mibBuilder.loadTexts:aniDevControlStartUpload.setStatus(_A)
class _AniDevControlUploadState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('successful',1),('failed',2)))
_AniDevControlUploadState_Type.__name__=_B
_AniDevControlUploadState_Object=MibScalar
aniDevControlUploadState=_AniDevControlUploadState_Object((1,3,6,1,4,1,4325,2,4,4),_AniDevControlUploadState_Type())
aniDevControlUploadState.setMaxAccess(_D)
if mibBuilder.loadTexts:aniDevControlUploadState.setStatus(_A)
mibBuilder.exportSymbols('DEVCONTROL-MIB',**{'aniDevControl':aniDevControl,'aniDevControlResetDevice':aniDevControlResetDevice,'aniDevControlSetFactoryDefaults':aniDevControlSetFactoryDefaults,'aniDevControlStartUpload':aniDevControlStartUpload,'aniDevControlUploadState':aniDevControlUploadState})