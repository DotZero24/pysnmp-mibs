_L='connection-forbidden'
_K='connection-bylocalloginpwd'
_J='connection-bydefault'
_I='read-only'
_H='tacacspSrvPriority'
_G='BIANCA-BRICK-TACACSP-MIB'
_F='DisplayString'
_E='disabled'
_D='enabled'
_C='read-write'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
_Bintec_ObjectIdentity=ObjectIdentity
bintec=_Bintec_ObjectIdentity((1,3,6,1,4,1,272))
_Bintecsec_ObjectIdentity=ObjectIdentity
bintecsec=_Bintecsec_ObjectIdentity((1,3,6,1,4,1,272,254))
_Tacacsp_ObjectIdentity=ObjectIdentity
tacacsp=_Tacacsp_ObjectIdentity((1,3,6,1,4,1,272,254,13))
_TacacspServerTable_Object=MibTable
tacacspServerTable=_TacacspServerTable_Object((1,3,6,1,4,1,272,254,13,1))
if mibBuilder.loadTexts:tacacspServerTable.setStatus(_A)
_TacacspServerEntry_Object=MibTableRow
tacacspServerEntry=_TacacspServerEntry_Object((1,3,6,1,4,1,272,254,13,1,1))
tacacspServerEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:tacacspServerEntry.setStatus(_A)
class _TacacspSrvPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_TacacspSrvPriority_Type.__name__=_B
_TacacspSrvPriority_Object=MibTableColumn
tacacspSrvPriority=_TacacspSrvPriority_Object((1,3,6,1,4,1,272,254,13,1,1,1),_TacacspSrvPriority_Type())
tacacspSrvPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:tacacspSrvPriority.setStatus(_A)
_TacacspSrvAddress_Type=IpAddress
_TacacspSrvAddress_Object=MibTableColumn
tacacspSrvAddress=_TacacspSrvAddress_Object((1,3,6,1,4,1,272,254,13,1,1,2),_TacacspSrvAddress_Type())
tacacspSrvAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tacacspSrvAddress.setStatus(_A)
class _TacacspSrvTcpPort_Type(Integer32):defaultValue=49
_TacacspSrvTcpPort_Type.__name__=_B
_TacacspSrvTcpPort_Object=MibTableColumn
tacacspSrvTcpPort=_TacacspSrvTcpPort_Object((1,3,6,1,4,1,272,254,13,1,1,3),_TacacspSrvTcpPort_Type())
tacacspSrvTcpPort.setMaxAccess(_I)
if mibBuilder.loadTexts:tacacspSrvTcpPort.setStatus(_A)
class _TacacspSrvSecret_Type(DisplayString):defaultValue=OctetString('')
_TacacspSrvSecret_Type.__name__=_F
_TacacspSrvSecret_Object=MibTableColumn
tacacspSrvSecret=_TacacspSrvSecret_Object((1,3,6,1,4,1,272,254,13,1,1,4),_TacacspSrvSecret_Type())
tacacspSrvSecret.setMaxAccess(_C)
if mibBuilder.loadTexts:tacacspSrvSecret.setStatus(_A)
class _TacacspSrvTimeout_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_TacacspSrvTimeout_Type.__name__=_B
_TacacspSrvTimeout_Object=MibTableColumn
tacacspSrvTimeout=_TacacspSrvTimeout_Object((1,3,6,1,4,1,272,254,13,1,1,5),_TacacspSrvTimeout_Type())
tacacspSrvTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:tacacspSrvTimeout.setStatus(_A)
class _TacacspSrvAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('delete',3)))
_TacacspSrvAdminStatus_Type.__name__=_B
_TacacspSrvAdminStatus_Object=MibTableColumn
tacacspSrvAdminStatus=_TacacspSrvAdminStatus_Object((1,3,6,1,4,1,272,254,13,1,1,7),_TacacspSrvAdminStatus_Type())
tacacspSrvAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tacacspSrvAdminStatus.setStatus(_A)
class _TacacspSrvOperStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('blocked',2),('down',3)))
_TacacspSrvOperStatus_Type.__name__=_B
_TacacspSrvOperStatus_Object=MibTableColumn
tacacspSrvOperStatus=_TacacspSrvOperStatus_Object((1,3,6,1,4,1,272,254,13,1,1,8),_TacacspSrvOperStatus_Type())
tacacspSrvOperStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:tacacspSrvOperStatus.setStatus(_A)
class _TacacspSrvPolicy_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('authoritative',1),('non-authoritative',2)))
_TacacspSrvPolicy_Type.__name__=_B
_TacacspSrvPolicy_Object=MibTableColumn
tacacspSrvPolicy=_TacacspSrvPolicy_Object((1,3,6,1,4,1,272,254,13,1,1,9),_TacacspSrvPolicy_Type())
tacacspSrvPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:tacacspSrvPolicy.setStatus(_A)
class _TacacspSrvEncrMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('encrypt',1),('cleartext',2)))
_TacacspSrvEncrMode_Type.__name__=_B
_TacacspSrvEncrMode_Object=MibTableColumn
tacacspSrvEncrMode=_TacacspSrvEncrMode_Object((1,3,6,1,4,1,272,254,13,1,1,10),_TacacspSrvEncrMode_Type())
tacacspSrvEncrMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tacacspSrvEncrMode.setStatus(_A)
class _TacacspSrvMultiSession_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_TacacspSrvMultiSession_Type.__name__=_B
_TacacspSrvMultiSession_Object=MibTableColumn
tacacspSrvMultiSession=_TacacspSrvMultiSession_Object((1,3,6,1,4,1,272,254,13,1,1,11),_TacacspSrvMultiSession_Type())
tacacspSrvMultiSession.setMaxAccess(_C)
if mibBuilder.loadTexts:tacacspSrvMultiSession.setStatus(_A)
class _TacacspSrvPppAuth_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_TacacspSrvPppAuth_Type.__name__=_B
_TacacspSrvPppAuth_Object=MibTableColumn
tacacspSrvPppAuth=_TacacspSrvPppAuth_Object((1,3,6,1,4,1,272,254,13,1,1,13),_TacacspSrvPppAuth_Type())
tacacspSrvPppAuth.setMaxAccess(_C)
if mibBuilder.loadTexts:tacacspSrvPppAuth.setStatus(_A)
class _TacacspSrvLoginAuth_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_TacacspSrvLoginAuth_Type.__name__=_B
_TacacspSrvLoginAuth_Object=MibTableColumn
tacacspSrvLoginAuth=_TacacspSrvLoginAuth_Object((1,3,6,1,4,1,272,254,13,1,1,14),_TacacspSrvLoginAuth_Type())
tacacspSrvLoginAuth.setMaxAccess(_C)
if mibBuilder.loadTexts:tacacspSrvLoginAuth.setStatus(_A)
class _TacacspSrvAccounting_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_TacacspSrvAccounting_Type.__name__=_B
_TacacspSrvAccounting_Object=MibTableColumn
tacacspSrvAccounting=_TacacspSrvAccounting_Object((1,3,6,1,4,1,272,254,13,1,1,15),_TacacspSrvAccounting_Type())
tacacspSrvAccounting.setMaxAccess(_C)
if mibBuilder.loadTexts:tacacspSrvAccounting.setStatus(_A)
class _TacacspSrvBlockTimeout_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_TacacspSrvBlockTimeout_Type.__name__=_B
_TacacspSrvBlockTimeout_Object=MibTableColumn
tacacspSrvBlockTimeout=_TacacspSrvBlockTimeout_Object((1,3,6,1,4,1,272,254,13,1,1,16),_TacacspSrvBlockTimeout_Type())
tacacspSrvBlockTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:tacacspSrvBlockTimeout.setStatus(_A)
class _TacacspSrvAuthentNoResp_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3)))
_TacacspSrvAuthentNoResp_Type.__name__=_B
_TacacspSrvAuthentNoResp_Object=MibTableColumn
tacacspSrvAuthentNoResp=_TacacspSrvAuthentNoResp_Object((1,3,6,1,4,1,272,254,13,1,1,17),_TacacspSrvAuthentNoResp_Type())
tacacspSrvAuthentNoResp.setMaxAccess(_C)
if mibBuilder.loadTexts:tacacspSrvAuthentNoResp.setStatus(_A)
class _TacacspSrvAuthentNegResp_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3)))
_TacacspSrvAuthentNegResp_Type.__name__=_B
_TacacspSrvAuthentNegResp_Object=MibTableColumn
tacacspSrvAuthentNegResp=_TacacspSrvAuthentNegResp_Object((1,3,6,1,4,1,272,254,13,1,1,18),_TacacspSrvAuthentNegResp_Type())
tacacspSrvAuthentNegResp.setMaxAccess(_C)
if mibBuilder.loadTexts:tacacspSrvAuthentNegResp.setStatus(_A)
class _TacacspSrvPrivLvlOnLogin_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,15))
_TacacspSrvPrivLvlOnLogin_Type.__name__=_B
_TacacspSrvPrivLvlOnLogin_Object=MibTableColumn
tacacspSrvPrivLvlOnLogin=_TacacspSrvPrivLvlOnLogin_Object((1,3,6,1,4,1,272,254,13,1,1,19),_TacacspSrvPrivLvlOnLogin_Type())
tacacspSrvPrivLvlOnLogin.setMaxAccess(_C)
if mibBuilder.loadTexts:tacacspSrvPrivLvlOnLogin.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'bintec':bintec,'bintecsec':bintecsec,'tacacsp':tacacsp,'tacacspServerTable':tacacspServerTable,'tacacspServerEntry':tacacspServerEntry,_H:tacacspSrvPriority,'tacacspSrvAddress':tacacspSrvAddress,'tacacspSrvTcpPort':tacacspSrvTcpPort,'tacacspSrvSecret':tacacspSrvSecret,'tacacspSrvTimeout':tacacspSrvTimeout,'tacacspSrvAdminStatus':tacacspSrvAdminStatus,'tacacspSrvOperStatus':tacacspSrvOperStatus,'tacacspSrvPolicy':tacacspSrvPolicy,'tacacspSrvEncrMode':tacacspSrvEncrMode,'tacacspSrvMultiSession':tacacspSrvMultiSession,'tacacspSrvPppAuth':tacacspSrvPppAuth,'tacacspSrvLoginAuth':tacacspSrvLoginAuth,'tacacspSrvAccounting':tacacspSrvAccounting,'tacacspSrvBlockTimeout':tacacspSrvBlockTimeout,'tacacspSrvAuthentNoResp':tacacspSrvAuthentNoResp,'tacacspSrvAuthentNegResp':tacacspSrvAuthentNegResp,'tacacspSrvPrivLvlOnLogin':tacacspSrvPrivLvlOnLogin})