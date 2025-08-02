_t='radiusAccServExtMIBGroup'
_s='radiusAccServMIBGroup'
_r='radiusAccServerCounterDiscontinuity'
_q='radiusAccServExtUnknownTypes'
_p='radiusAccServExtNoRecords'
_o='radiusAccServExtMalformedRequests'
_n='radiusAccServExtBadAuthenticators'
_m='radiusAccServExtResponses'
_l='radiusAccServExtDupRequests'
_k='radiusAccServExtRequests'
_j='radiusAccServExtPacketsDropped'
_i='radiusAccClientExtID'
_h='radiusAccClientInetAddress'
_g='radiusAccClientInetAddressType'
_f='radiusAccServUnknownTypes'
_e='radiusAccServNoRecords'
_d='radiusAccServMalformedRequests'
_c='radiusAccServBadAuthenticators'
_b='radiusAccServResponses'
_a='radiusAccServDupRequests'
_Z='radiusAccServRequests'
_Y='radiusAccServPacketsDropped'
_X='radiusAccClientID'
_W='radiusAccClientAddress'
_V='radiusAccClientExtIndex'
_U='not-accessible'
_T='radiusAccClientIndex'
_S='radiusAccServTotalUnknownTypes'
_R='radiusAccServTotalNoRecords'
_Q='radiusAccServTotalPacketsDropped'
_P='radiusAccServTotalBadAuthenticators'
_O='radiusAccServTotalMalformedRequests'
_N='radiusAccServTotalResponses'
_M='radiusAccServTotalDupRequests'
_L='radiusAccServTotalInvalidRequests'
_K='radiusAccServTotalRequests'
_J='radiusAccServConfigReset'
_I='radiusAccServResetTime'
_H='radiusAccServUpTime'
_G='radiusAccServIdent'
_F='Integer32'
_E='deprecated'
_D='packets'
_C='current'
_B='read-only'
_A='RADIUS-ACC-SERVER-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
radiusAccServMIB=ModuleIdentity((1,3,6,1,2,1,67,2,1))
if mibBuilder.loadTexts:radiusAccServMIB.setRevisions(('2006-08-21 00:00','1999-06-11 00:00'))
_RadiusMIB_ObjectIdentity=ObjectIdentity
radiusMIB=_RadiusMIB_ObjectIdentity((1,3,6,1,2,1,67))
if mibBuilder.loadTexts:radiusMIB.setStatus(_C)
_RadiusAccounting_ObjectIdentity=ObjectIdentity
radiusAccounting=_RadiusAccounting_ObjectIdentity((1,3,6,1,2,1,67,2))
_RadiusAccServMIBObjects_ObjectIdentity=ObjectIdentity
radiusAccServMIBObjects=_RadiusAccServMIBObjects_ObjectIdentity((1,3,6,1,2,1,67,2,1,1))
_RadiusAccServ_ObjectIdentity=ObjectIdentity
radiusAccServ=_RadiusAccServ_ObjectIdentity((1,3,6,1,2,1,67,2,1,1,1))
_RadiusAccServIdent_Type=SnmpAdminString
_RadiusAccServIdent_Object=MibScalar
radiusAccServIdent=_RadiusAccServIdent_Object((1,3,6,1,2,1,67,2,1,1,1,1),_RadiusAccServIdent_Type())
radiusAccServIdent.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServIdent.setStatus(_C)
_RadiusAccServUpTime_Type=TimeTicks
_RadiusAccServUpTime_Object=MibScalar
radiusAccServUpTime=_RadiusAccServUpTime_Object((1,3,6,1,2,1,67,2,1,1,1,2),_RadiusAccServUpTime_Type())
radiusAccServUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServUpTime.setStatus(_C)
_RadiusAccServResetTime_Type=TimeTicks
_RadiusAccServResetTime_Object=MibScalar
radiusAccServResetTime=_RadiusAccServResetTime_Object((1,3,6,1,2,1,67,2,1,1,1,3),_RadiusAccServResetTime_Type())
radiusAccServResetTime.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServResetTime.setStatus(_C)
class _RadiusAccServConfigReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('reset',2),('initializing',3),('running',4)))
_RadiusAccServConfigReset_Type.__name__=_F
_RadiusAccServConfigReset_Object=MibScalar
radiusAccServConfigReset=_RadiusAccServConfigReset_Object((1,3,6,1,2,1,67,2,1,1,1,4),_RadiusAccServConfigReset_Type())
radiusAccServConfigReset.setMaxAccess('read-write')
if mibBuilder.loadTexts:radiusAccServConfigReset.setStatus(_C)
_RadiusAccServTotalRequests_Type=Counter32
_RadiusAccServTotalRequests_Object=MibScalar
radiusAccServTotalRequests=_RadiusAccServTotalRequests_Object((1,3,6,1,2,1,67,2,1,1,1,5),_RadiusAccServTotalRequests_Type())
radiusAccServTotalRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServTotalRequests.setStatus(_C)
if mibBuilder.loadTexts:radiusAccServTotalRequests.setUnits(_D)
_RadiusAccServTotalInvalidRequests_Type=Counter32
_RadiusAccServTotalInvalidRequests_Object=MibScalar
radiusAccServTotalInvalidRequests=_RadiusAccServTotalInvalidRequests_Object((1,3,6,1,2,1,67,2,1,1,1,6),_RadiusAccServTotalInvalidRequests_Type())
radiusAccServTotalInvalidRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServTotalInvalidRequests.setStatus(_C)
if mibBuilder.loadTexts:radiusAccServTotalInvalidRequests.setUnits(_D)
_RadiusAccServTotalDupRequests_Type=Counter32
_RadiusAccServTotalDupRequests_Object=MibScalar
radiusAccServTotalDupRequests=_RadiusAccServTotalDupRequests_Object((1,3,6,1,2,1,67,2,1,1,1,7),_RadiusAccServTotalDupRequests_Type())
radiusAccServTotalDupRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServTotalDupRequests.setStatus(_C)
if mibBuilder.loadTexts:radiusAccServTotalDupRequests.setUnits(_D)
_RadiusAccServTotalResponses_Type=Counter32
_RadiusAccServTotalResponses_Object=MibScalar
radiusAccServTotalResponses=_RadiusAccServTotalResponses_Object((1,3,6,1,2,1,67,2,1,1,1,8),_RadiusAccServTotalResponses_Type())
radiusAccServTotalResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServTotalResponses.setStatus(_C)
if mibBuilder.loadTexts:radiusAccServTotalResponses.setUnits(_D)
_RadiusAccServTotalMalformedRequests_Type=Counter32
_RadiusAccServTotalMalformedRequests_Object=MibScalar
radiusAccServTotalMalformedRequests=_RadiusAccServTotalMalformedRequests_Object((1,3,6,1,2,1,67,2,1,1,1,9),_RadiusAccServTotalMalformedRequests_Type())
radiusAccServTotalMalformedRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServTotalMalformedRequests.setStatus(_C)
if mibBuilder.loadTexts:radiusAccServTotalMalformedRequests.setUnits(_D)
_RadiusAccServTotalBadAuthenticators_Type=Counter32
_RadiusAccServTotalBadAuthenticators_Object=MibScalar
radiusAccServTotalBadAuthenticators=_RadiusAccServTotalBadAuthenticators_Object((1,3,6,1,2,1,67,2,1,1,1,10),_RadiusAccServTotalBadAuthenticators_Type())
radiusAccServTotalBadAuthenticators.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServTotalBadAuthenticators.setStatus(_C)
if mibBuilder.loadTexts:radiusAccServTotalBadAuthenticators.setUnits(_D)
_RadiusAccServTotalPacketsDropped_Type=Counter32
_RadiusAccServTotalPacketsDropped_Object=MibScalar
radiusAccServTotalPacketsDropped=_RadiusAccServTotalPacketsDropped_Object((1,3,6,1,2,1,67,2,1,1,1,11),_RadiusAccServTotalPacketsDropped_Type())
radiusAccServTotalPacketsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServTotalPacketsDropped.setStatus(_C)
if mibBuilder.loadTexts:radiusAccServTotalPacketsDropped.setUnits(_D)
_RadiusAccServTotalNoRecords_Type=Counter32
_RadiusAccServTotalNoRecords_Object=MibScalar
radiusAccServTotalNoRecords=_RadiusAccServTotalNoRecords_Object((1,3,6,1,2,1,67,2,1,1,1,12),_RadiusAccServTotalNoRecords_Type())
radiusAccServTotalNoRecords.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServTotalNoRecords.setStatus(_C)
if mibBuilder.loadTexts:radiusAccServTotalNoRecords.setUnits(_D)
_RadiusAccServTotalUnknownTypes_Type=Counter32
_RadiusAccServTotalUnknownTypes_Object=MibScalar
radiusAccServTotalUnknownTypes=_RadiusAccServTotalUnknownTypes_Object((1,3,6,1,2,1,67,2,1,1,1,13),_RadiusAccServTotalUnknownTypes_Type())
radiusAccServTotalUnknownTypes.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServTotalUnknownTypes.setStatus(_C)
if mibBuilder.loadTexts:radiusAccServTotalUnknownTypes.setUnits(_D)
_RadiusAccClientTable_Object=MibTable
radiusAccClientTable=_RadiusAccClientTable_Object((1,3,6,1,2,1,67,2,1,1,1,14))
if mibBuilder.loadTexts:radiusAccClientTable.setStatus(_E)
_RadiusAccClientEntry_Object=MibTableRow
radiusAccClientEntry=_RadiusAccClientEntry_Object((1,3,6,1,2,1,67,2,1,1,1,14,1))
radiusAccClientEntry.setIndexNames((0,_A,_T))
if mibBuilder.loadTexts:radiusAccClientEntry.setStatus(_E)
class _RadiusAccClientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RadiusAccClientIndex_Type.__name__=_F
_RadiusAccClientIndex_Object=MibTableColumn
radiusAccClientIndex=_RadiusAccClientIndex_Object((1,3,6,1,2,1,67,2,1,1,1,14,1,1),_RadiusAccClientIndex_Type())
radiusAccClientIndex.setMaxAccess(_U)
if mibBuilder.loadTexts:radiusAccClientIndex.setStatus(_E)
_RadiusAccClientAddress_Type=IpAddress
_RadiusAccClientAddress_Object=MibTableColumn
radiusAccClientAddress=_RadiusAccClientAddress_Object((1,3,6,1,2,1,67,2,1,1,1,14,1,2),_RadiusAccClientAddress_Type())
radiusAccClientAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccClientAddress.setStatus(_E)
_RadiusAccClientID_Type=SnmpAdminString
_RadiusAccClientID_Object=MibTableColumn
radiusAccClientID=_RadiusAccClientID_Object((1,3,6,1,2,1,67,2,1,1,1,14,1,3),_RadiusAccClientID_Type())
radiusAccClientID.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccClientID.setStatus(_E)
_RadiusAccServPacketsDropped_Type=Counter32
_RadiusAccServPacketsDropped_Object=MibTableColumn
radiusAccServPacketsDropped=_RadiusAccServPacketsDropped_Object((1,3,6,1,2,1,67,2,1,1,1,14,1,4),_RadiusAccServPacketsDropped_Type())
radiusAccServPacketsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServPacketsDropped.setStatus(_E)
if mibBuilder.loadTexts:radiusAccServPacketsDropped.setUnits(_D)
_RadiusAccServRequests_Type=Counter32
_RadiusAccServRequests_Object=MibTableColumn
radiusAccServRequests=_RadiusAccServRequests_Object((1,3,6,1,2,1,67,2,1,1,1,14,1,5),_RadiusAccServRequests_Type())
radiusAccServRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServRequests.setStatus(_E)
if mibBuilder.loadTexts:radiusAccServRequests.setUnits(_D)
_RadiusAccServDupRequests_Type=Counter32
_RadiusAccServDupRequests_Object=MibTableColumn
radiusAccServDupRequests=_RadiusAccServDupRequests_Object((1,3,6,1,2,1,67,2,1,1,1,14,1,6),_RadiusAccServDupRequests_Type())
radiusAccServDupRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServDupRequests.setStatus(_E)
if mibBuilder.loadTexts:radiusAccServDupRequests.setUnits(_D)
_RadiusAccServResponses_Type=Counter32
_RadiusAccServResponses_Object=MibTableColumn
radiusAccServResponses=_RadiusAccServResponses_Object((1,3,6,1,2,1,67,2,1,1,1,14,1,7),_RadiusAccServResponses_Type())
radiusAccServResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServResponses.setStatus(_E)
if mibBuilder.loadTexts:radiusAccServResponses.setUnits(_D)
_RadiusAccServBadAuthenticators_Type=Counter32
_RadiusAccServBadAuthenticators_Object=MibTableColumn
radiusAccServBadAuthenticators=_RadiusAccServBadAuthenticators_Object((1,3,6,1,2,1,67,2,1,1,1,14,1,8),_RadiusAccServBadAuthenticators_Type())
radiusAccServBadAuthenticators.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServBadAuthenticators.setStatus(_E)
if mibBuilder.loadTexts:radiusAccServBadAuthenticators.setUnits(_D)
_RadiusAccServMalformedRequests_Type=Counter32
_RadiusAccServMalformedRequests_Object=MibTableColumn
radiusAccServMalformedRequests=_RadiusAccServMalformedRequests_Object((1,3,6,1,2,1,67,2,1,1,1,14,1,9),_RadiusAccServMalformedRequests_Type())
radiusAccServMalformedRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServMalformedRequests.setStatus(_E)
if mibBuilder.loadTexts:radiusAccServMalformedRequests.setUnits(_D)
_RadiusAccServNoRecords_Type=Counter32
_RadiusAccServNoRecords_Object=MibTableColumn
radiusAccServNoRecords=_RadiusAccServNoRecords_Object((1,3,6,1,2,1,67,2,1,1,1,14,1,10),_RadiusAccServNoRecords_Type())
radiusAccServNoRecords.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServNoRecords.setStatus(_E)
if mibBuilder.loadTexts:radiusAccServNoRecords.setUnits(_D)
_RadiusAccServUnknownTypes_Type=Counter32
_RadiusAccServUnknownTypes_Object=MibTableColumn
radiusAccServUnknownTypes=_RadiusAccServUnknownTypes_Object((1,3,6,1,2,1,67,2,1,1,1,14,1,11),_RadiusAccServUnknownTypes_Type())
radiusAccServUnknownTypes.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServUnknownTypes.setStatus(_E)
if mibBuilder.loadTexts:radiusAccServUnknownTypes.setUnits(_D)
_RadiusAccClientExtTable_Object=MibTable
radiusAccClientExtTable=_RadiusAccClientExtTable_Object((1,3,6,1,2,1,67,2,1,1,1,15))
if mibBuilder.loadTexts:radiusAccClientExtTable.setStatus(_C)
_RadiusAccClientExtEntry_Object=MibTableRow
radiusAccClientExtEntry=_RadiusAccClientExtEntry_Object((1,3,6,1,2,1,67,2,1,1,1,15,1))
radiusAccClientExtEntry.setIndexNames((0,_A,_V))
if mibBuilder.loadTexts:radiusAccClientExtEntry.setStatus(_C)
class _RadiusAccClientExtIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RadiusAccClientExtIndex_Type.__name__=_F
_RadiusAccClientExtIndex_Object=MibTableColumn
radiusAccClientExtIndex=_RadiusAccClientExtIndex_Object((1,3,6,1,2,1,67,2,1,1,1,15,1,1),_RadiusAccClientExtIndex_Type())
radiusAccClientExtIndex.setMaxAccess(_U)
if mibBuilder.loadTexts:radiusAccClientExtIndex.setStatus(_C)
_RadiusAccClientInetAddressType_Type=InetAddressType
_RadiusAccClientInetAddressType_Object=MibTableColumn
radiusAccClientInetAddressType=_RadiusAccClientInetAddressType_Object((1,3,6,1,2,1,67,2,1,1,1,15,1,2),_RadiusAccClientInetAddressType_Type())
radiusAccClientInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccClientInetAddressType.setStatus(_C)
_RadiusAccClientInetAddress_Type=InetAddress
_RadiusAccClientInetAddress_Object=MibTableColumn
radiusAccClientInetAddress=_RadiusAccClientInetAddress_Object((1,3,6,1,2,1,67,2,1,1,1,15,1,3),_RadiusAccClientInetAddress_Type())
radiusAccClientInetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccClientInetAddress.setStatus(_C)
_RadiusAccClientExtID_Type=SnmpAdminString
_RadiusAccClientExtID_Object=MibTableColumn
radiusAccClientExtID=_RadiusAccClientExtID_Object((1,3,6,1,2,1,67,2,1,1,1,15,1,4),_RadiusAccClientExtID_Type())
radiusAccClientExtID.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccClientExtID.setStatus(_C)
_RadiusAccServExtPacketsDropped_Type=Counter32
_RadiusAccServExtPacketsDropped_Object=MibTableColumn
radiusAccServExtPacketsDropped=_RadiusAccServExtPacketsDropped_Object((1,3,6,1,2,1,67,2,1,1,1,15,1,5),_RadiusAccServExtPacketsDropped_Type())
radiusAccServExtPacketsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServExtPacketsDropped.setStatus(_C)
if mibBuilder.loadTexts:radiusAccServExtPacketsDropped.setUnits(_D)
_RadiusAccServExtRequests_Type=Counter32
_RadiusAccServExtRequests_Object=MibTableColumn
radiusAccServExtRequests=_RadiusAccServExtRequests_Object((1,3,6,1,2,1,67,2,1,1,1,15,1,6),_RadiusAccServExtRequests_Type())
radiusAccServExtRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServExtRequests.setStatus(_C)
if mibBuilder.loadTexts:radiusAccServExtRequests.setUnits(_D)
_RadiusAccServExtDupRequests_Type=Counter32
_RadiusAccServExtDupRequests_Object=MibTableColumn
radiusAccServExtDupRequests=_RadiusAccServExtDupRequests_Object((1,3,6,1,2,1,67,2,1,1,1,15,1,7),_RadiusAccServExtDupRequests_Type())
radiusAccServExtDupRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServExtDupRequests.setStatus(_C)
if mibBuilder.loadTexts:radiusAccServExtDupRequests.setUnits(_D)
_RadiusAccServExtResponses_Type=Counter32
_RadiusAccServExtResponses_Object=MibTableColumn
radiusAccServExtResponses=_RadiusAccServExtResponses_Object((1,3,6,1,2,1,67,2,1,1,1,15,1,8),_RadiusAccServExtResponses_Type())
radiusAccServExtResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServExtResponses.setStatus(_C)
if mibBuilder.loadTexts:radiusAccServExtResponses.setUnits(_D)
_RadiusAccServExtBadAuthenticators_Type=Counter32
_RadiusAccServExtBadAuthenticators_Object=MibTableColumn
radiusAccServExtBadAuthenticators=_RadiusAccServExtBadAuthenticators_Object((1,3,6,1,2,1,67,2,1,1,1,15,1,9),_RadiusAccServExtBadAuthenticators_Type())
radiusAccServExtBadAuthenticators.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServExtBadAuthenticators.setStatus(_C)
if mibBuilder.loadTexts:radiusAccServExtBadAuthenticators.setUnits(_D)
_RadiusAccServExtMalformedRequests_Type=Counter32
_RadiusAccServExtMalformedRequests_Object=MibTableColumn
radiusAccServExtMalformedRequests=_RadiusAccServExtMalformedRequests_Object((1,3,6,1,2,1,67,2,1,1,1,15,1,10),_RadiusAccServExtMalformedRequests_Type())
radiusAccServExtMalformedRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServExtMalformedRequests.setStatus(_C)
if mibBuilder.loadTexts:radiusAccServExtMalformedRequests.setUnits(_D)
_RadiusAccServExtNoRecords_Type=Counter32
_RadiusAccServExtNoRecords_Object=MibTableColumn
radiusAccServExtNoRecords=_RadiusAccServExtNoRecords_Object((1,3,6,1,2,1,67,2,1,1,1,15,1,11),_RadiusAccServExtNoRecords_Type())
radiusAccServExtNoRecords.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServExtNoRecords.setStatus(_C)
if mibBuilder.loadTexts:radiusAccServExtNoRecords.setUnits(_D)
_RadiusAccServExtUnknownTypes_Type=Counter32
_RadiusAccServExtUnknownTypes_Object=MibTableColumn
radiusAccServExtUnknownTypes=_RadiusAccServExtUnknownTypes_Object((1,3,6,1,2,1,67,2,1,1,1,15,1,12),_RadiusAccServExtUnknownTypes_Type())
radiusAccServExtUnknownTypes.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServExtUnknownTypes.setStatus(_C)
if mibBuilder.loadTexts:radiusAccServExtUnknownTypes.setUnits(_D)
_RadiusAccServerCounterDiscontinuity_Type=TimeTicks
_RadiusAccServerCounterDiscontinuity_Object=MibTableColumn
radiusAccServerCounterDiscontinuity=_RadiusAccServerCounterDiscontinuity_Object((1,3,6,1,2,1,67,2,1,1,1,15,1,13),_RadiusAccServerCounterDiscontinuity_Type())
radiusAccServerCounterDiscontinuity.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccServerCounterDiscontinuity.setStatus(_C)
if mibBuilder.loadTexts:radiusAccServerCounterDiscontinuity.setUnits('centiseconds')
_RadiusAccServMIBConformance_ObjectIdentity=ObjectIdentity
radiusAccServMIBConformance=_RadiusAccServMIBConformance_ObjectIdentity((1,3,6,1,2,1,67,2,1,2))
_RadiusAccServMIBCompliances_ObjectIdentity=ObjectIdentity
radiusAccServMIBCompliances=_RadiusAccServMIBCompliances_ObjectIdentity((1,3,6,1,2,1,67,2,1,2,1))
_RadiusAccServMIBGroups_ObjectIdentity=ObjectIdentity
radiusAccServMIBGroups=_RadiusAccServMIBGroups_ObjectIdentity((1,3,6,1,2,1,67,2,1,2,2))
radiusAccServMIBGroup=ObjectGroup((1,3,6,1,2,1,67,2,1,2,2,1))
radiusAccServMIBGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:radiusAccServMIBGroup.setStatus(_E)
radiusAccServExtMIBGroup=ObjectGroup((1,3,6,1,2,1,67,2,1,2,2,2))
radiusAccServExtMIBGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:radiusAccServExtMIBGroup.setStatus(_C)
radiusAccServMIBCompliance=ModuleCompliance((1,3,6,1,2,1,67,2,1,2,1,1))
radiusAccServMIBCompliance.setObjects((_A,_s))
if mibBuilder.loadTexts:radiusAccServMIBCompliance.setStatus(_E)
radiusAccServExtMIBCompliance=ModuleCompliance((1,3,6,1,2,1,67,2,1,2,1,2))
radiusAccServExtMIBCompliance.setObjects((_A,_t))
if mibBuilder.loadTexts:radiusAccServExtMIBCompliance.setStatus(_C)
mibBuilder.exportSymbols(_A,**{'radiusMIB':radiusMIB,'radiusAccounting':radiusAccounting,'radiusAccServMIB':radiusAccServMIB,'radiusAccServMIBObjects':radiusAccServMIBObjects,'radiusAccServ':radiusAccServ,_G:radiusAccServIdent,_H:radiusAccServUpTime,_I:radiusAccServResetTime,_J:radiusAccServConfigReset,_K:radiusAccServTotalRequests,_L:radiusAccServTotalInvalidRequests,_M:radiusAccServTotalDupRequests,_N:radiusAccServTotalResponses,_O:radiusAccServTotalMalformedRequests,_P:radiusAccServTotalBadAuthenticators,_Q:radiusAccServTotalPacketsDropped,_R:radiusAccServTotalNoRecords,_S:radiusAccServTotalUnknownTypes,'radiusAccClientTable':radiusAccClientTable,'radiusAccClientEntry':radiusAccClientEntry,_T:radiusAccClientIndex,_W:radiusAccClientAddress,_X:radiusAccClientID,_Y:radiusAccServPacketsDropped,_Z:radiusAccServRequests,_a:radiusAccServDupRequests,_b:radiusAccServResponses,_c:radiusAccServBadAuthenticators,_d:radiusAccServMalformedRequests,_e:radiusAccServNoRecords,_f:radiusAccServUnknownTypes,'radiusAccClientExtTable':radiusAccClientExtTable,'radiusAccClientExtEntry':radiusAccClientExtEntry,_V:radiusAccClientExtIndex,_g:radiusAccClientInetAddressType,_h:radiusAccClientInetAddress,_i:radiusAccClientExtID,_j:radiusAccServExtPacketsDropped,_k:radiusAccServExtRequests,_l:radiusAccServExtDupRequests,_m:radiusAccServExtResponses,_n:radiusAccServExtBadAuthenticators,_o:radiusAccServExtMalformedRequests,_p:radiusAccServExtNoRecords,_q:radiusAccServExtUnknownTypes,_r:radiusAccServerCounterDiscontinuity,'radiusAccServMIBConformance':radiusAccServMIBConformance,'radiusAccServMIBCompliances':radiusAccServMIBCompliances,'radiusAccServMIBCompliance':radiusAccServMIBCompliance,'radiusAccServExtMIBCompliance':radiusAccServExtMIBCompliance,'radiusAccServMIBGroups':radiusAccServMIBGroups,_s:radiusAccServMIBGroup,_t:radiusAccServExtMIBGroup})