_p='sipServerRegistrarUsersGroup'
_o='sipServerRegistrarStatsGroup'
_n='sipServerRegistrarConfigGroup'
_m='sipServerProxyStatsGroup'
_l='sipServerProxyConfigGroup'
_k='sipServerRegContactPreference'
_j='sipServerRegContactExpiry'
_i='sipServerRegContactLastUpdated'
_h='sipServerRegContactURI'
_g='sipServerRegContactDisplayName'
_f='sipServerRegUserDisconTime'
_e='sipServerRegUserAuthenticationFailures'
_d='sipServerRegUserUri'
_c='sipServerRegStatsDisconTime'
_b='sipServerRegStatsRejectedRegs'
_a='sipServerRegStatsAcceptedRegs'
_Z='sipServerRegDfltRegActiveInterval'
_Y='sipServerRegCurrentUsers'
_X='sipServerRegMaxUsers'
_W='sipServerRegMaxContactExpiryDuration'
_V='sipServerProxyStatsDisconTime'
_U='sipServerProxyStatProxyReqFailures'
_T='sipServerCfgProxyAuthDefaultRealm'
_S='sipServerCfgProxyAuthMethod'
_R='sipServerCfgProxyRecordRoute'
_Q='sipServerCfgProxyRecursion'
_P='sipServerCfgProxyStatefulness'
_O='sipServerCfgHostAddress'
_N='sipServerCfgHostAddressType'
_M='sipServerRegContactIndex'
_L='not-accessible'
_K='seconds'
_J='Integer32'
_I='Gauge32'
_H='sipServerRegUserIndex'
_G='sipServerConfigGroup'
_F='Unsigned32'
_E='applIndex'
_D='NETWORK-SERVICES-MIB'
_C='read-only'
_B='SIP-SERVER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
applIndex,=mibBuilder.importSymbols(_D,_E)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_I,_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso','mib-2')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
sipServerMIB=ModuleIdentity((1,3,6,1,2,1,151))
if mibBuilder.loadTexts:sipServerMIB.setRevisions(('2007-04-20 00:00',))
_SipServerMIBObjects_ObjectIdentity=ObjectIdentity
sipServerMIBObjects=_SipServerMIBObjects_ObjectIdentity((1,3,6,1,2,1,151,1))
_SipServerCfg_ObjectIdentity=ObjectIdentity
sipServerCfg=_SipServerCfg_ObjectIdentity((1,3,6,1,2,1,151,1,1))
_SipServerCfgTable_Object=MibTable
sipServerCfgTable=_SipServerCfgTable_Object((1,3,6,1,2,1,151,1,1,1))
if mibBuilder.loadTexts:sipServerCfgTable.setStatus(_A)
_SipServerCfgEntry_Object=MibTableRow
sipServerCfgEntry=_SipServerCfgEntry_Object((1,3,6,1,2,1,151,1,1,1,1))
sipServerCfgEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:sipServerCfgEntry.setStatus(_A)
_SipServerCfgHostAddressType_Type=InetAddressType
_SipServerCfgHostAddressType_Object=MibTableColumn
sipServerCfgHostAddressType=_SipServerCfgHostAddressType_Object((1,3,6,1,2,1,151,1,1,1,1,1),_SipServerCfgHostAddressType_Type())
sipServerCfgHostAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:sipServerCfgHostAddressType.setStatus(_A)
_SipServerCfgHostAddress_Type=InetAddress
_SipServerCfgHostAddress_Object=MibTableColumn
sipServerCfgHostAddress=_SipServerCfgHostAddress_Object((1,3,6,1,2,1,151,1,1,1,1,2),_SipServerCfgHostAddress_Type())
sipServerCfgHostAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sipServerCfgHostAddress.setStatus(_A)
_SipServerProxyCfg_ObjectIdentity=ObjectIdentity
sipServerProxyCfg=_SipServerProxyCfg_ObjectIdentity((1,3,6,1,2,1,151,1,3))
_SipServerProxyCfgTable_Object=MibTable
sipServerProxyCfgTable=_SipServerProxyCfgTable_Object((1,3,6,1,2,1,151,1,3,1))
if mibBuilder.loadTexts:sipServerProxyCfgTable.setStatus(_A)
_SipServerProxyCfgEntry_Object=MibTableRow
sipServerProxyCfgEntry=_SipServerProxyCfgEntry_Object((1,3,6,1,2,1,151,1,3,1,1))
sipServerProxyCfgEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:sipServerProxyCfgEntry.setStatus(_A)
class _SipServerCfgProxyStatefulness_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('stateless',1),('transactionStateful',2),('callStateful',3)))
_SipServerCfgProxyStatefulness_Type.__name__=_J
_SipServerCfgProxyStatefulness_Object=MibTableColumn
sipServerCfgProxyStatefulness=_SipServerCfgProxyStatefulness_Object((1,3,6,1,2,1,151,1,3,1,1,1),_SipServerCfgProxyStatefulness_Type())
sipServerCfgProxyStatefulness.setMaxAccess(_C)
if mibBuilder.loadTexts:sipServerCfgProxyStatefulness.setStatus(_A)
_SipServerCfgProxyRecursion_Type=TruthValue
_SipServerCfgProxyRecursion_Object=MibTableColumn
sipServerCfgProxyRecursion=_SipServerCfgProxyRecursion_Object((1,3,6,1,2,1,151,1,3,1,1,2),_SipServerCfgProxyRecursion_Type())
sipServerCfgProxyRecursion.setMaxAccess(_C)
if mibBuilder.loadTexts:sipServerCfgProxyRecursion.setStatus(_A)
_SipServerCfgProxyRecordRoute_Type=TruthValue
_SipServerCfgProxyRecordRoute_Object=MibTableColumn
sipServerCfgProxyRecordRoute=_SipServerCfgProxyRecordRoute_Object((1,3,6,1,2,1,151,1,3,1,1,3),_SipServerCfgProxyRecordRoute_Type())
sipServerCfgProxyRecordRoute.setMaxAccess(_C)
if mibBuilder.loadTexts:sipServerCfgProxyRecordRoute.setStatus(_A)
class _SipServerCfgProxyAuthMethod_Type(Bits):namedValues=NamedValues(*(('none',0),('tls',1),('digest',2)))
_SipServerCfgProxyAuthMethod_Type.__name__='Bits'
_SipServerCfgProxyAuthMethod_Object=MibTableColumn
sipServerCfgProxyAuthMethod=_SipServerCfgProxyAuthMethod_Object((1,3,6,1,2,1,151,1,3,1,1,4),_SipServerCfgProxyAuthMethod_Type())
sipServerCfgProxyAuthMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:sipServerCfgProxyAuthMethod.setStatus(_A)
_SipServerCfgProxyAuthDefaultRealm_Type=SnmpAdminString
_SipServerCfgProxyAuthDefaultRealm_Object=MibTableColumn
sipServerCfgProxyAuthDefaultRealm=_SipServerCfgProxyAuthDefaultRealm_Object((1,3,6,1,2,1,151,1,3,1,1,5),_SipServerCfgProxyAuthDefaultRealm_Type())
sipServerCfgProxyAuthDefaultRealm.setMaxAccess(_C)
if mibBuilder.loadTexts:sipServerCfgProxyAuthDefaultRealm.setStatus(_A)
_SipServerProxyStats_ObjectIdentity=ObjectIdentity
sipServerProxyStats=_SipServerProxyStats_ObjectIdentity((1,3,6,1,2,1,151,1,4))
_SipServerProxyStatsTable_Object=MibTable
sipServerProxyStatsTable=_SipServerProxyStatsTable_Object((1,3,6,1,2,1,151,1,4,1))
if mibBuilder.loadTexts:sipServerProxyStatsTable.setStatus(_A)
_SipServerProxyStatsEntry_Object=MibTableRow
sipServerProxyStatsEntry=_SipServerProxyStatsEntry_Object((1,3,6,1,2,1,151,1,4,1,1))
sipServerProxyStatsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:sipServerProxyStatsEntry.setStatus(_A)
_SipServerProxyStatProxyReqFailures_Type=Counter32
_SipServerProxyStatProxyReqFailures_Object=MibTableColumn
sipServerProxyStatProxyReqFailures=_SipServerProxyStatProxyReqFailures_Object((1,3,6,1,2,1,151,1,4,1,1,1),_SipServerProxyStatProxyReqFailures_Type())
sipServerProxyStatProxyReqFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:sipServerProxyStatProxyReqFailures.setStatus(_A)
_SipServerProxyStatsDisconTime_Type=TimeStamp
_SipServerProxyStatsDisconTime_Object=MibTableColumn
sipServerProxyStatsDisconTime=_SipServerProxyStatsDisconTime_Object((1,3,6,1,2,1,151,1,4,1,1,2),_SipServerProxyStatsDisconTime_Type())
sipServerProxyStatsDisconTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sipServerProxyStatsDisconTime.setStatus(_A)
_SipServerRegCfg_ObjectIdentity=ObjectIdentity
sipServerRegCfg=_SipServerRegCfg_ObjectIdentity((1,3,6,1,2,1,151,1,5))
_SipServerRegCfgTable_Object=MibTable
sipServerRegCfgTable=_SipServerRegCfgTable_Object((1,3,6,1,2,1,151,1,5,1))
if mibBuilder.loadTexts:sipServerRegCfgTable.setStatus(_A)
_SipServerRegCfgEntry_Object=MibTableRow
sipServerRegCfgEntry=_SipServerRegCfgEntry_Object((1,3,6,1,2,1,151,1,5,1,1))
sipServerRegCfgEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:sipServerRegCfgEntry.setStatus(_A)
class _SipServerRegMaxContactExpiryDuration_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_SipServerRegMaxContactExpiryDuration_Type.__name__=_F
_SipServerRegMaxContactExpiryDuration_Object=MibTableColumn
sipServerRegMaxContactExpiryDuration=_SipServerRegMaxContactExpiryDuration_Object((1,3,6,1,2,1,151,1,5,1,1,1),_SipServerRegMaxContactExpiryDuration_Type())
sipServerRegMaxContactExpiryDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:sipServerRegMaxContactExpiryDuration.setStatus(_A)
if mibBuilder.loadTexts:sipServerRegMaxContactExpiryDuration.setUnits(_K)
class _SipServerRegMaxUsers_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_SipServerRegMaxUsers_Type.__name__=_F
_SipServerRegMaxUsers_Object=MibTableColumn
sipServerRegMaxUsers=_SipServerRegMaxUsers_Object((1,3,6,1,2,1,151,1,5,1,1,2),_SipServerRegMaxUsers_Type())
sipServerRegMaxUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:sipServerRegMaxUsers.setStatus(_A)
class _SipServerRegCurrentUsers_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_SipServerRegCurrentUsers_Type.__name__=_I
_SipServerRegCurrentUsers_Object=MibTableColumn
sipServerRegCurrentUsers=_SipServerRegCurrentUsers_Object((1,3,6,1,2,1,151,1,5,1,1,3),_SipServerRegCurrentUsers_Type())
sipServerRegCurrentUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:sipServerRegCurrentUsers.setStatus(_A)
class _SipServerRegDfltRegActiveInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_SipServerRegDfltRegActiveInterval_Type.__name__=_F
_SipServerRegDfltRegActiveInterval_Object=MibTableColumn
sipServerRegDfltRegActiveInterval=_SipServerRegDfltRegActiveInterval_Object((1,3,6,1,2,1,151,1,5,1,1,4),_SipServerRegDfltRegActiveInterval_Type())
sipServerRegDfltRegActiveInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:sipServerRegDfltRegActiveInterval.setStatus(_A)
if mibBuilder.loadTexts:sipServerRegDfltRegActiveInterval.setUnits(_K)
_SipServerRegUserTable_Object=MibTable
sipServerRegUserTable=_SipServerRegUserTable_Object((1,3,6,1,2,1,151,1,5,2))
if mibBuilder.loadTexts:sipServerRegUserTable.setStatus(_A)
_SipServerRegUserEntry_Object=MibTableRow
sipServerRegUserEntry=_SipServerRegUserEntry_Object((1,3,6,1,2,1,151,1,5,2,1))
sipServerRegUserEntry.setIndexNames((0,_D,_E),(0,_B,_H))
if mibBuilder.loadTexts:sipServerRegUserEntry.setStatus(_A)
class _SipServerRegUserIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_SipServerRegUserIndex_Type.__name__=_F
_SipServerRegUserIndex_Object=MibTableColumn
sipServerRegUserIndex=_SipServerRegUserIndex_Object((1,3,6,1,2,1,151,1,5,2,1,1),_SipServerRegUserIndex_Type())
sipServerRegUserIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:sipServerRegUserIndex.setStatus(_A)
_SipServerRegUserUri_Type=SnmpAdminString
_SipServerRegUserUri_Object=MibTableColumn
sipServerRegUserUri=_SipServerRegUserUri_Object((1,3,6,1,2,1,151,1,5,2,1,2),_SipServerRegUserUri_Type())
sipServerRegUserUri.setMaxAccess(_C)
if mibBuilder.loadTexts:sipServerRegUserUri.setStatus(_A)
_SipServerRegUserAuthenticationFailures_Type=Counter32
_SipServerRegUserAuthenticationFailures_Object=MibTableColumn
sipServerRegUserAuthenticationFailures=_SipServerRegUserAuthenticationFailures_Object((1,3,6,1,2,1,151,1,5,2,1,3),_SipServerRegUserAuthenticationFailures_Type())
sipServerRegUserAuthenticationFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:sipServerRegUserAuthenticationFailures.setStatus(_A)
_SipServerRegUserDisconTime_Type=TimeStamp
_SipServerRegUserDisconTime_Object=MibTableColumn
sipServerRegUserDisconTime=_SipServerRegUserDisconTime_Object((1,3,6,1,2,1,151,1,5,2,1,4),_SipServerRegUserDisconTime_Type())
sipServerRegUserDisconTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sipServerRegUserDisconTime.setStatus(_A)
_SipServerRegContactTable_Object=MibTable
sipServerRegContactTable=_SipServerRegContactTable_Object((1,3,6,1,2,1,151,1,5,3))
if mibBuilder.loadTexts:sipServerRegContactTable.setStatus(_A)
_SipServerRegContactEntry_Object=MibTableRow
sipServerRegContactEntry=_SipServerRegContactEntry_Object((1,3,6,1,2,1,151,1,5,3,1))
sipServerRegContactEntry.setIndexNames((0,_D,_E),(0,_B,_H),(0,_B,_M))
if mibBuilder.loadTexts:sipServerRegContactEntry.setStatus(_A)
class _SipServerRegContactIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_SipServerRegContactIndex_Type.__name__=_F
_SipServerRegContactIndex_Object=MibTableColumn
sipServerRegContactIndex=_SipServerRegContactIndex_Object((1,3,6,1,2,1,151,1,5,3,1,1),_SipServerRegContactIndex_Type())
sipServerRegContactIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:sipServerRegContactIndex.setStatus(_A)
_SipServerRegContactDisplayName_Type=SnmpAdminString
_SipServerRegContactDisplayName_Object=MibTableColumn
sipServerRegContactDisplayName=_SipServerRegContactDisplayName_Object((1,3,6,1,2,1,151,1,5,3,1,2),_SipServerRegContactDisplayName_Type())
sipServerRegContactDisplayName.setMaxAccess(_C)
if mibBuilder.loadTexts:sipServerRegContactDisplayName.setStatus(_A)
_SipServerRegContactURI_Type=SnmpAdminString
_SipServerRegContactURI_Object=MibTableColumn
sipServerRegContactURI=_SipServerRegContactURI_Object((1,3,6,1,2,1,151,1,5,3,1,3),_SipServerRegContactURI_Type())
sipServerRegContactURI.setMaxAccess(_C)
if mibBuilder.loadTexts:sipServerRegContactURI.setStatus(_A)
_SipServerRegContactLastUpdated_Type=TimeStamp
_SipServerRegContactLastUpdated_Object=MibTableColumn
sipServerRegContactLastUpdated=_SipServerRegContactLastUpdated_Object((1,3,6,1,2,1,151,1,5,3,1,4),_SipServerRegContactLastUpdated_Type())
sipServerRegContactLastUpdated.setMaxAccess(_C)
if mibBuilder.loadTexts:sipServerRegContactLastUpdated.setStatus(_A)
_SipServerRegContactExpiry_Type=DateAndTime
_SipServerRegContactExpiry_Object=MibTableColumn
sipServerRegContactExpiry=_SipServerRegContactExpiry_Object((1,3,6,1,2,1,151,1,5,3,1,5),_SipServerRegContactExpiry_Type())
sipServerRegContactExpiry.setMaxAccess(_C)
if mibBuilder.loadTexts:sipServerRegContactExpiry.setStatus(_A)
_SipServerRegContactPreference_Type=SnmpAdminString
_SipServerRegContactPreference_Object=MibTableColumn
sipServerRegContactPreference=_SipServerRegContactPreference_Object((1,3,6,1,2,1,151,1,5,3,1,6),_SipServerRegContactPreference_Type())
sipServerRegContactPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:sipServerRegContactPreference.setStatus(_A)
_SipServerRegStats_ObjectIdentity=ObjectIdentity
sipServerRegStats=_SipServerRegStats_ObjectIdentity((1,3,6,1,2,1,151,1,6))
_SipServerRegStatsTable_Object=MibTable
sipServerRegStatsTable=_SipServerRegStatsTable_Object((1,3,6,1,2,1,151,1,6,1))
if mibBuilder.loadTexts:sipServerRegStatsTable.setStatus(_A)
_SipServerRegStatsEntry_Object=MibTableRow
sipServerRegStatsEntry=_SipServerRegStatsEntry_Object((1,3,6,1,2,1,151,1,6,1,1))
sipServerRegStatsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:sipServerRegStatsEntry.setStatus(_A)
_SipServerRegStatsAcceptedRegs_Type=Counter32
_SipServerRegStatsAcceptedRegs_Object=MibTableColumn
sipServerRegStatsAcceptedRegs=_SipServerRegStatsAcceptedRegs_Object((1,3,6,1,2,1,151,1,6,1,1,1),_SipServerRegStatsAcceptedRegs_Type())
sipServerRegStatsAcceptedRegs.setMaxAccess(_C)
if mibBuilder.loadTexts:sipServerRegStatsAcceptedRegs.setStatus(_A)
_SipServerRegStatsRejectedRegs_Type=Counter32
_SipServerRegStatsRejectedRegs_Object=MibTableColumn
sipServerRegStatsRejectedRegs=_SipServerRegStatsRejectedRegs_Object((1,3,6,1,2,1,151,1,6,1,1,2),_SipServerRegStatsRejectedRegs_Type())
sipServerRegStatsRejectedRegs.setMaxAccess(_C)
if mibBuilder.loadTexts:sipServerRegStatsRejectedRegs.setStatus(_A)
_SipServerRegStatsDisconTime_Type=TimeStamp
_SipServerRegStatsDisconTime_Object=MibTableColumn
sipServerRegStatsDisconTime=_SipServerRegStatsDisconTime_Object((1,3,6,1,2,1,151,1,6,1,1,3),_SipServerRegStatsDisconTime_Type())
sipServerRegStatsDisconTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sipServerRegStatsDisconTime.setStatus(_A)
_SipServerMIBConformance_ObjectIdentity=ObjectIdentity
sipServerMIBConformance=_SipServerMIBConformance_ObjectIdentity((1,3,6,1,2,1,151,2))
_SipServerMIBCompliances_ObjectIdentity=ObjectIdentity
sipServerMIBCompliances=_SipServerMIBCompliances_ObjectIdentity((1,3,6,1,2,1,151,2,1))
_SipServerMIBGroups_ObjectIdentity=ObjectIdentity
sipServerMIBGroups=_SipServerMIBGroups_ObjectIdentity((1,3,6,1,2,1,151,2,2))
sipServerConfigGroup=ObjectGroup((1,3,6,1,2,1,151,2,2,1))
sipServerConfigGroup.setObjects(*((_B,_N),(_B,_O)))
if mibBuilder.loadTexts:sipServerConfigGroup.setStatus(_A)
sipServerProxyConfigGroup=ObjectGroup((1,3,6,1,2,1,151,2,2,2))
sipServerProxyConfigGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:sipServerProxyConfigGroup.setStatus(_A)
sipServerProxyStatsGroup=ObjectGroup((1,3,6,1,2,1,151,2,2,3))
sipServerProxyStatsGroup.setObjects(*((_B,_U),(_B,_V)))
if mibBuilder.loadTexts:sipServerProxyStatsGroup.setStatus(_A)
sipServerRegistrarConfigGroup=ObjectGroup((1,3,6,1,2,1,151,2,2,4))
sipServerRegistrarConfigGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:sipServerRegistrarConfigGroup.setStatus(_A)
sipServerRegistrarStatsGroup=ObjectGroup((1,3,6,1,2,1,151,2,2,5))
sipServerRegistrarStatsGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:sipServerRegistrarStatsGroup.setStatus(_A)
sipServerRegistrarUsersGroup=ObjectGroup((1,3,6,1,2,1,151,2,2,6))
sipServerRegistrarUsersGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:sipServerRegistrarUsersGroup.setStatus(_A)
sipServerProxyServerCompliance=ModuleCompliance((1,3,6,1,2,1,151,2,1,1))
sipServerProxyServerCompliance.setObjects(*((_B,_G),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:sipServerProxyServerCompliance.setStatus(_A)
sipRedirectServerCompliance=ModuleCompliance((1,3,6,1,2,1,151,2,1,2))
sipRedirectServerCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:sipRedirectServerCompliance.setStatus(_A)
sipServerRegistrarServerCompliance=ModuleCompliance((1,3,6,1,2,1,151,2,1,3))
sipServerRegistrarServerCompliance.setObjects(*((_B,_G),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:sipServerRegistrarServerCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'sipServerMIB':sipServerMIB,'sipServerMIBObjects':sipServerMIBObjects,'sipServerCfg':sipServerCfg,'sipServerCfgTable':sipServerCfgTable,'sipServerCfgEntry':sipServerCfgEntry,_N:sipServerCfgHostAddressType,_O:sipServerCfgHostAddress,'sipServerProxyCfg':sipServerProxyCfg,'sipServerProxyCfgTable':sipServerProxyCfgTable,'sipServerProxyCfgEntry':sipServerProxyCfgEntry,_P:sipServerCfgProxyStatefulness,_Q:sipServerCfgProxyRecursion,_R:sipServerCfgProxyRecordRoute,_S:sipServerCfgProxyAuthMethod,_T:sipServerCfgProxyAuthDefaultRealm,'sipServerProxyStats':sipServerProxyStats,'sipServerProxyStatsTable':sipServerProxyStatsTable,'sipServerProxyStatsEntry':sipServerProxyStatsEntry,_U:sipServerProxyStatProxyReqFailures,_V:sipServerProxyStatsDisconTime,'sipServerRegCfg':sipServerRegCfg,'sipServerRegCfgTable':sipServerRegCfgTable,'sipServerRegCfgEntry':sipServerRegCfgEntry,_W:sipServerRegMaxContactExpiryDuration,_X:sipServerRegMaxUsers,_Y:sipServerRegCurrentUsers,_Z:sipServerRegDfltRegActiveInterval,'sipServerRegUserTable':sipServerRegUserTable,'sipServerRegUserEntry':sipServerRegUserEntry,_H:sipServerRegUserIndex,_d:sipServerRegUserUri,_e:sipServerRegUserAuthenticationFailures,_f:sipServerRegUserDisconTime,'sipServerRegContactTable':sipServerRegContactTable,'sipServerRegContactEntry':sipServerRegContactEntry,_M:sipServerRegContactIndex,_g:sipServerRegContactDisplayName,_h:sipServerRegContactURI,_i:sipServerRegContactLastUpdated,_j:sipServerRegContactExpiry,_k:sipServerRegContactPreference,'sipServerRegStats':sipServerRegStats,'sipServerRegStatsTable':sipServerRegStatsTable,'sipServerRegStatsEntry':sipServerRegStatsEntry,_a:sipServerRegStatsAcceptedRegs,_b:sipServerRegStatsRejectedRegs,_c:sipServerRegStatsDisconTime,'sipServerMIBConformance':sipServerMIBConformance,'sipServerMIBCompliances':sipServerMIBCompliances,'sipServerProxyServerCompliance':sipServerProxyServerCompliance,'sipRedirectServerCompliance':sipRedirectServerCompliance,'sipServerRegistrarServerCompliance':sipServerRegistrarServerCompliance,'sipServerMIBGroups':sipServerMIBGroups,_G:sipServerConfigGroup,_l:sipServerProxyConfigGroup,_m:sipServerProxyStatsGroup,_n:sipServerRegistrarConfigGroup,_o:sipServerRegistrarStatsGroup,_p:sipServerRegistrarUsersGroup})