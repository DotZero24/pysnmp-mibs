_G='minutes'
_F='Integer32'
_E='OctetString'
_D='Unsigned32'
_C='DisplayString'
_B='current'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ruckusCommonUpgradeModule,=mibBuilder.importSymbols('RUCKUS-ROOT-MIB','ruckusCommonUpgradeModule')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_C,'PhysAddress','TextualConvention','TruthValue')
ruckusUpgradeMIB=ModuleIdentity((1,3,6,1,4,1,25053,1,1,5,1))
_RuckusUpgradeObjects_ObjectIdentity=ObjectIdentity
ruckusUpgradeObjects=_RuckusUpgradeObjects_ObjectIdentity((1,3,6,1,4,1,25053,1,1,5,1,1))
_RuckusFileTransfer_ObjectIdentity=ObjectIdentity
ruckusFileTransfer=_RuckusFileTransfer_ObjectIdentity((1,3,6,1,4,1,25053,1,1,5,1,1,1))
class _RuckusFileTransferMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tftp',1),('ftp',2),('web',3)))
_RuckusFileTransferMethod_Type.__name__=_F
_RuckusFileTransferMethod_Object=MibScalar
ruckusFileTransferMethod=_RuckusFileTransferMethod_Object((1,3,6,1,4,1,25053,1,1,5,1,1,1,1),_RuckusFileTransferMethod_Type())
ruckusFileTransferMethod.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusFileTransferMethod.setStatus(_B)
_RuckusFileTransferHostName_Type=DisplayString
_RuckusFileTransferHostName_Object=MibScalar
ruckusFileTransferHostName=_RuckusFileTransferHostName_Object((1,3,6,1,4,1,25053,1,1,5,1,1,1,2),_RuckusFileTransferHostName_Type())
ruckusFileTransferHostName.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusFileTransferHostName.setStatus(_B)
class _RuckusFileTransferHostAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,40))
_RuckusFileTransferHostAddr_Type.__name__=_E
_RuckusFileTransferHostAddr_Object=MibScalar
ruckusFileTransferHostAddr=_RuckusFileTransferHostAddr_Object((1,3,6,1,4,1,25053,1,1,5,1,1,1,3),_RuckusFileTransferHostAddr_Type())
ruckusFileTransferHostAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusFileTransferHostAddr.setStatus(_B)
class _RuckusFileTransferControlFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_RuckusFileTransferControlFileName_Type.__name__=_C
_RuckusFileTransferControlFileName_Object=MibScalar
ruckusFileTransferControlFileName=_RuckusFileTransferControlFileName_Object((1,3,6,1,4,1,25053,1,1,5,1,1,1,4),_RuckusFileTransferControlFileName_Type())
ruckusFileTransferControlFileName.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusFileTransferControlFileName.setStatus(_B)
class _RuckusFileTransferFTPUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RuckusFileTransferFTPUsername_Type.__name__=_C
_RuckusFileTransferFTPUsername_Object=MibScalar
ruckusFileTransferFTPUsername=_RuckusFileTransferFTPUsername_Object((1,3,6,1,4,1,25053,1,1,5,1,1,1,5),_RuckusFileTransferFTPUsername_Type())
ruckusFileTransferFTPUsername.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusFileTransferFTPUsername.setStatus(_B)
class _RuckusFileTransferFTPPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RuckusFileTransferFTPPassword_Type.__name__=_C
_RuckusFileTransferFTPPassword_Object=MibScalar
ruckusFileTransferFTPPassword=_RuckusFileTransferFTPPassword_Object((1,3,6,1,4,1,25053,1,1,5,1,1,1,6),_RuckusFileTransferFTPPassword_Type())
ruckusFileTransferFTPPassword.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusFileTransferFTPPassword.setStatus(_B)
_RuckusFileTransferUpgradeNow_Type=TruthValue
_RuckusFileTransferUpgradeNow_Object=MibScalar
ruckusFileTransferUpgradeNow=_RuckusFileTransferUpgradeNow_Object((1,3,6,1,4,1,25053,1,1,5,1,1,1,7),_RuckusFileTransferUpgradeNow_Type())
ruckusFileTransferUpgradeNow.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusFileTransferUpgradeNow.setStatus(_B)
_RuckusFileTransferTakeEffectImmediately_Type=TruthValue
_RuckusFileTransferTakeEffectImmediately_Object=MibScalar
ruckusFileTransferTakeEffectImmediately=_RuckusFileTransferTakeEffectImmediately_Object((1,3,6,1,4,1,25053,1,1,5,1,1,1,8),_RuckusFileTransferTakeEffectImmediately_Type())
ruckusFileTransferTakeEffectImmediately.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusFileTransferTakeEffectImmediately.setStatus(_B)
_RuckusAutoUpgrade_ObjectIdentity=ObjectIdentity
ruckusAutoUpgrade=_RuckusAutoUpgrade_ObjectIdentity((1,3,6,1,4,1,25053,1,1,5,1,1,2))
class _RuckusAutoUpgradeInitialCheckInterval_Type(Unsigned32):defaultValue=5
_RuckusAutoUpgradeInitialCheckInterval_Type.__name__=_D
_RuckusAutoUpgradeInitialCheckInterval_Object=MibScalar
ruckusAutoUpgradeInitialCheckInterval=_RuckusAutoUpgradeInitialCheckInterval_Object((1,3,6,1,4,1,25053,1,1,5,1,1,2,1),_RuckusAutoUpgradeInitialCheckInterval_Type())
ruckusAutoUpgradeInitialCheckInterval.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusAutoUpgradeInitialCheckInterval.setStatus(_B)
if mibBuilder.loadTexts:ruckusAutoUpgradeInitialCheckInterval.setUnits(_G)
class _RuckusAutoUpgradeCheckInterval_Type(Unsigned32):defaultValue=720
_RuckusAutoUpgradeCheckInterval_Type.__name__=_D
_RuckusAutoUpgradeCheckInterval_Object=MibScalar
ruckusAutoUpgradeCheckInterval=_RuckusAutoUpgradeCheckInterval_Object((1,3,6,1,4,1,25053,1,1,5,1,1,2,2),_RuckusAutoUpgradeCheckInterval_Type())
ruckusAutoUpgradeCheckInterval.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusAutoUpgradeCheckInterval.setStatus(_B)
if mibBuilder.loadTexts:ruckusAutoUpgradeCheckInterval.setUnits(_G)
_RuckusAutoUpgradeStatus_Type=Unsigned32
_RuckusAutoUpgradeStatus_Object=MibScalar
ruckusAutoUpgradeStatus=_RuckusAutoUpgradeStatus_Object((1,3,6,1,4,1,25053,1,1,5,1,1,2,3),_RuckusAutoUpgradeStatus_Type())
ruckusAutoUpgradeStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusAutoUpgradeStatus.setStatus(_B)
mibBuilder.exportSymbols('RUCKUS-UPGRADE-MIB',**{'ruckusUpgradeMIB':ruckusUpgradeMIB,'ruckusUpgradeObjects':ruckusUpgradeObjects,'ruckusFileTransfer':ruckusFileTransfer,'ruckusFileTransferMethod':ruckusFileTransferMethod,'ruckusFileTransferHostName':ruckusFileTransferHostName,'ruckusFileTransferHostAddr':ruckusFileTransferHostAddr,'ruckusFileTransferControlFileName':ruckusFileTransferControlFileName,'ruckusFileTransferFTPUsername':ruckusFileTransferFTPUsername,'ruckusFileTransferFTPPassword':ruckusFileTransferFTPPassword,'ruckusFileTransferUpgradeNow':ruckusFileTransferUpgradeNow,'ruckusFileTransferTakeEffectImmediately':ruckusFileTransferTakeEffectImmediately,'ruckusAutoUpgrade':ruckusAutoUpgrade,'ruckusAutoUpgradeInitialCheckInterval':ruckusAutoUpgradeInitialCheckInterval,'ruckusAutoUpgradeCheckInterval':ruckusAutoUpgradeCheckInterval,'ruckusAutoUpgradeStatus':ruckusAutoUpgradeStatus})