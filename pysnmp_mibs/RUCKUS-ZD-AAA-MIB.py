_F='ruckusZDAAAConfigID'
_E='RUCKUS-ZD-AAA-MIB'
_D='OctetString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
ruckusZDWLANModule,=mibBuilder.importSymbols('RUCKUS-ROOT-MIB','ruckusZDWLANModule')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ruckusZDAAAMIB=ModuleIdentity((1,3,6,1,4,1,25053,1,2,2,3))
_RuckusZDAAAObjects_ObjectIdentity=ObjectIdentity
ruckusZDAAAObjects=_RuckusZDAAAObjects_ObjectIdentity((1,3,6,1,4,1,25053,1,2,2,3,1))
_RuckusZDAAAConfig_ObjectIdentity=ObjectIdentity
ruckusZDAAAConfig=_RuckusZDAAAConfig_ObjectIdentity((1,3,6,1,4,1,25053,1,2,2,3,1,1))
_RuckusZDAAAConfigTable_Object=MibTable
ruckusZDAAAConfigTable=_RuckusZDAAAConfigTable_Object((1,3,6,1,4,1,25053,1,2,2,3,1,1,1))
if mibBuilder.loadTexts:ruckusZDAAAConfigTable.setStatus(_A)
_RuckusZDAAAConfigEntry_Object=MibTableRow
ruckusZDAAAConfigEntry=_RuckusZDAAAConfigEntry_Object((1,3,6,1,4,1,25053,1,2,2,3,1,1,1,1))
ruckusZDAAAConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ruckusZDAAAConfigEntry.setStatus(_A)
class _RuckusZDAAAConfigID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,32))
_RuckusZDAAAConfigID_Type.__name__=_C
_RuckusZDAAAConfigID_Object=MibTableColumn
ruckusZDAAAConfigID=_RuckusZDAAAConfigID_Object((1,3,6,1,4,1,25053,1,2,2,3,1,1,1,1,1),_RuckusZDAAAConfigID_Type())
ruckusZDAAAConfigID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ruckusZDAAAConfigID.setStatus(_A)
class _RuckusZDAAAConfigName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_RuckusZDAAAConfigName_Type.__name__=_D
_RuckusZDAAAConfigName_Object=MibTableColumn
ruckusZDAAAConfigName=_RuckusZDAAAConfigName_Object((1,3,6,1,4,1,25053,1,2,2,3,1,1,1,1,2),_RuckusZDAAAConfigName_Type())
ruckusZDAAAConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAAAConfigName.setStatus(_A)
class _RuckusZDAAAConfigServiceType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('active-directory',1),('ldap-directory',2),('aaa-authentication',3),('aaa-accounting',4)))
_RuckusZDAAAConfigServiceType_Type.__name__=_C
_RuckusZDAAAConfigServiceType_Object=MibTableColumn
ruckusZDAAAConfigServiceType=_RuckusZDAAAConfigServiceType_Object((1,3,6,1,4,1,25053,1,2,2,3,1,1,1,1,3),_RuckusZDAAAConfigServiceType_Type())
ruckusZDAAAConfigServiceType.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAAAConfigServiceType.setStatus(_A)
_RuckusZDAAAConfigRowStatus_Type=RowStatus
_RuckusZDAAAConfigRowStatus_Object=MibTableColumn
ruckusZDAAAConfigRowStatus=_RuckusZDAAAConfigRowStatus_Object((1,3,6,1,4,1,25053,1,2,2,3,1,1,1,1,10),_RuckusZDAAAConfigRowStatus_Type())
ruckusZDAAAConfigRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:ruckusZDAAAConfigRowStatus.setStatus(_A)
_RuckusZDAAASvrTable_Object=MibTable
ruckusZDAAASvrTable=_RuckusZDAAASvrTable_Object((1,3,6,1,4,1,25053,1,2,2,3,1,1,2))
if mibBuilder.loadTexts:ruckusZDAAASvrTable.setStatus(_A)
_RuckusZDAAASvrEntry_Object=MibTableRow
ruckusZDAAASvrEntry=_RuckusZDAAASvrEntry_Object((1,3,6,1,4,1,25053,1,2,2,3,1,1,2,1))
ruckusZDAAASvrEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ruckusZDAAASvrEntry.setStatus(_A)
class _RuckusZDAAARadiusBackupControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_RuckusZDAAARadiusBackupControl_Type.__name__=_C
_RuckusZDAAARadiusBackupControl_Object=MibTableColumn
ruckusZDAAARadiusBackupControl=_RuckusZDAAARadiusBackupControl_Object((1,3,6,1,4,1,25053,1,2,2,3,1,1,2,1,5),_RuckusZDAAARadiusBackupControl_Type())
ruckusZDAAARadiusBackupControl.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAAARadiusBackupControl.setStatus(_A)
class _RuckusZDAAARadiusPrimarySvrIpAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,40))
_RuckusZDAAARadiusPrimarySvrIpAddress_Type.__name__=_D
_RuckusZDAAARadiusPrimarySvrIpAddress_Object=MibTableColumn
ruckusZDAAARadiusPrimarySvrIpAddress=_RuckusZDAAARadiusPrimarySvrIpAddress_Object((1,3,6,1,4,1,25053,1,2,2,3,1,1,2,1,10),_RuckusZDAAARadiusPrimarySvrIpAddress_Type())
ruckusZDAAARadiusPrimarySvrIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAAARadiusPrimarySvrIpAddress.setStatus(_A)
_RuckusZDAAARadiusPrimarySvrPort_Type=Integer32
_RuckusZDAAARadiusPrimarySvrPort_Object=MibTableColumn
ruckusZDAAARadiusPrimarySvrPort=_RuckusZDAAARadiusPrimarySvrPort_Object((1,3,6,1,4,1,25053,1,2,2,3,1,1,2,1,11),_RuckusZDAAARadiusPrimarySvrPort_Type())
ruckusZDAAARadiusPrimarySvrPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAAARadiusPrimarySvrPort.setStatus(_A)
class _RuckusZDAAARadiusPrimarySvrPasswd_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RuckusZDAAARadiusPrimarySvrPasswd_Type.__name__=_D
_RuckusZDAAARadiusPrimarySvrPasswd_Object=MibTableColumn
ruckusZDAAARadiusPrimarySvrPasswd=_RuckusZDAAARadiusPrimarySvrPasswd_Object((1,3,6,1,4,1,25053,1,2,2,3,1,1,2,1,12),_RuckusZDAAARadiusPrimarySvrPasswd_Type())
ruckusZDAAARadiusPrimarySvrPasswd.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAAARadiusPrimarySvrPasswd.setStatus(_A)
class _RuckusZDAAARadiusSecondarySvrIpAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,40))
_RuckusZDAAARadiusSecondarySvrIpAddress_Type.__name__=_D
_RuckusZDAAARadiusSecondarySvrIpAddress_Object=MibTableColumn
ruckusZDAAARadiusSecondarySvrIpAddress=_RuckusZDAAARadiusSecondarySvrIpAddress_Object((1,3,6,1,4,1,25053,1,2,2,3,1,1,2,1,15),_RuckusZDAAARadiusSecondarySvrIpAddress_Type())
ruckusZDAAARadiusSecondarySvrIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAAARadiusSecondarySvrIpAddress.setStatus(_A)
_RuckusZDAAARadiusSecondarySvrPort_Type=Integer32
_RuckusZDAAARadiusSecondarySvrPort_Object=MibTableColumn
ruckusZDAAARadiusSecondarySvrPort=_RuckusZDAAARadiusSecondarySvrPort_Object((1,3,6,1,4,1,25053,1,2,2,3,1,1,2,1,16),_RuckusZDAAARadiusSecondarySvrPort_Type())
ruckusZDAAARadiusSecondarySvrPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAAARadiusSecondarySvrPort.setStatus(_A)
class _RuckusZDAAARadiusSecondarySvrPasswd_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RuckusZDAAARadiusSecondarySvrPasswd_Type.__name__=_D
_RuckusZDAAARadiusSecondarySvrPasswd_Object=MibTableColumn
ruckusZDAAARadiusSecondarySvrPasswd=_RuckusZDAAARadiusSecondarySvrPasswd_Object((1,3,6,1,4,1,25053,1,2,2,3,1,1,2,1,17),_RuckusZDAAARadiusSecondarySvrPasswd_Type())
ruckusZDAAARadiusSecondarySvrPasswd.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAAARadiusSecondarySvrPasswd.setStatus(_A)
class _RuckusZDAAARadiusFailoverTimeout_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,20))
_RuckusZDAAARadiusFailoverTimeout_Type.__name__=_C
_RuckusZDAAARadiusFailoverTimeout_Object=MibTableColumn
ruckusZDAAARadiusFailoverTimeout=_RuckusZDAAARadiusFailoverTimeout_Object((1,3,6,1,4,1,25053,1,2,2,3,1,1,2,1,20),_RuckusZDAAARadiusFailoverTimeout_Type())
ruckusZDAAARadiusFailoverTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAAARadiusFailoverTimeout.setStatus(_A)
class _RuckusZDAAARadiusFailoverRetry_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_RuckusZDAAARadiusFailoverRetry_Type.__name__=_C
_RuckusZDAAARadiusFailoverRetry_Object=MibTableColumn
ruckusZDAAARadiusFailoverRetry=_RuckusZDAAARadiusFailoverRetry_Object((1,3,6,1,4,1,25053,1,2,2,3,1,1,2,1,21),_RuckusZDAAARadiusFailoverRetry_Type())
ruckusZDAAARadiusFailoverRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAAARadiusFailoverRetry.setStatus(_A)
class _RuckusZDAAARadiusFailoverReconnectPrimary_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_RuckusZDAAARadiusFailoverReconnectPrimary_Type.__name__=_C
_RuckusZDAAARadiusFailoverReconnectPrimary_Object=MibTableColumn
ruckusZDAAARadiusFailoverReconnectPrimary=_RuckusZDAAARadiusFailoverReconnectPrimary_Object((1,3,6,1,4,1,25053,1,2,2,3,1,1,2,1,22),_RuckusZDAAARadiusFailoverReconnectPrimary_Type())
ruckusZDAAARadiusFailoverReconnectPrimary.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAAARadiusFailoverReconnectPrimary.setStatus(_A)
class _RuckusZDAAARadiusFailoverConsecutiveDropPkts_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_RuckusZDAAARadiusFailoverConsecutiveDropPkts_Type.__name__=_C
_RuckusZDAAARadiusFailoverConsecutiveDropPkts_Object=MibTableColumn
ruckusZDAAARadiusFailoverConsecutiveDropPkts=_RuckusZDAAARadiusFailoverConsecutiveDropPkts_Object((1,3,6,1,4,1,25053,1,2,2,3,1,1,2,1,23),_RuckusZDAAARadiusFailoverConsecutiveDropPkts_Type())
ruckusZDAAARadiusFailoverConsecutiveDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAAARadiusFailoverConsecutiveDropPkts.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ruckusZDAAAMIB':ruckusZDAAAMIB,'ruckusZDAAAObjects':ruckusZDAAAObjects,'ruckusZDAAAConfig':ruckusZDAAAConfig,'ruckusZDAAAConfigTable':ruckusZDAAAConfigTable,'ruckusZDAAAConfigEntry':ruckusZDAAAConfigEntry,_F:ruckusZDAAAConfigID,'ruckusZDAAAConfigName':ruckusZDAAAConfigName,'ruckusZDAAAConfigServiceType':ruckusZDAAAConfigServiceType,'ruckusZDAAAConfigRowStatus':ruckusZDAAAConfigRowStatus,'ruckusZDAAASvrTable':ruckusZDAAASvrTable,'ruckusZDAAASvrEntry':ruckusZDAAASvrEntry,'ruckusZDAAARadiusBackupControl':ruckusZDAAARadiusBackupControl,'ruckusZDAAARadiusPrimarySvrIpAddress':ruckusZDAAARadiusPrimarySvrIpAddress,'ruckusZDAAARadiusPrimarySvrPort':ruckusZDAAARadiusPrimarySvrPort,'ruckusZDAAARadiusPrimarySvrPasswd':ruckusZDAAARadiusPrimarySvrPasswd,'ruckusZDAAARadiusSecondarySvrIpAddress':ruckusZDAAARadiusSecondarySvrIpAddress,'ruckusZDAAARadiusSecondarySvrPort':ruckusZDAAARadiusSecondarySvrPort,'ruckusZDAAARadiusSecondarySvrPasswd':ruckusZDAAARadiusSecondarySvrPasswd,'ruckusZDAAARadiusFailoverTimeout':ruckusZDAAARadiusFailoverTimeout,'ruckusZDAAARadiusFailoverRetry':ruckusZDAAARadiusFailoverRetry,'ruckusZDAAARadiusFailoverReconnectPrimary':ruckusZDAAARadiusFailoverReconnectPrimary,'ruckusZDAAARadiusFailoverConsecutiveDropPkts':ruckusZDAAARadiusFailoverConsecutiveDropPkts})