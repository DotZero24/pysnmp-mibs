_F='Unsigned32'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap','MxEnableState','MxIpAddress','MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort','MxIpHostNamePort','MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mohMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1550))
_MohMIBObjects_ObjectIdentity=ObjectIdentity
mohMIBObjects=_MohMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1550,1))
class _FileUrl_Type(OctetString):defaultValue=OctetString('')
_FileUrl_Type.__name__=_B
_FileUrl_Object=MibScalar
fileUrl=_FileUrl_Object((1,3,6,1,4,1,4935,1000,100,200,100,1550,1,100),_FileUrl_Type())
fileUrl.setMaxAccess(_D)
if mibBuilder.loadTexts:fileUrl.setStatus(_A)
class _Username_Type(OctetString):defaultValue=OctetString('')
_Username_Type.__name__=_B
_Username_Object=MibScalar
username=_Username_Object((1,3,6,1,4,1,4935,1000,100,200,100,1550,1,200),_Username_Type())
username.setMaxAccess(_D)
if mibBuilder.loadTexts:username.setStatus(_A)
class _Password_Type(OctetString):defaultValue=OctetString('')
_Password_Type.__name__=_B
_Password_Object=MibScalar
password=_Password_Object((1,3,6,1,4,1,4935,1000,100,200,100,1550,1,300),_Password_Type())
password.setMaxAccess(_D)
if mibBuilder.loadTexts:password.setStatus(_A)
class _ReloadInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6000))
_ReloadInterval_Type.__name__=_F
_ReloadInterval_Object=MibScalar
reloadInterval=_ReloadInterval_Object((1,3,6,1,4,1,4935,1000,100,200,100,1550,1,400),_ReloadInterval_Type())
reloadInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:reloadInterval.setStatus(_A)
class _FileStatus_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500)));namedValues=NamedValues(*(('noFile',100),('fileReady',200),('downloading',300),('invalidFormat',400),('fileTooLarge',500)))
_FileStatus_Type.__name__=_C
_FileStatus_Object=MibScalar
fileStatus=_FileStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,1550,1,500),_FileStatus_Type())
fileStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fileStatus.setStatus(_A)
class _LastTransferStatus_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('success',100),('failed',200)))
_LastTransferStatus_Type.__name__=_C
_LastTransferStatus_Object=MibScalar
lastTransferStatus=_LastTransferStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,1550,1,600),_LastTransferStatus_Type())
lastTransferStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:lastTransferStatus.setStatus(_A)
class _LastTransferDateTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LastTransferDateTime_Type.__name__=_B
_LastTransferDateTime_Object=MibScalar
lastTransferDateTime=_LastTransferDateTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1550,1,700),_LastTransferDateTime_Type())
lastTransferDateTime.setMaxAccess(_E)
if mibBuilder.loadTexts:lastTransferDateTime.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1550,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*(('disable',0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_C
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,1550,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1550,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_C
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,1550,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_E)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols('MX-MOH-MIB',**{'mohMIB':mohMIB,'mohMIBObjects':mohMIBObjects,'fileUrl':fileUrl,'username':username,'password':password,'reloadInterval':reloadInterval,'fileStatus':fileStatus,'lastTransferStatus':lastTransferStatus,'lastTransferDateTime':lastTransferDateTime,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})