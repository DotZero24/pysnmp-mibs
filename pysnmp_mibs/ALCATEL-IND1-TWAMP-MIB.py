_R='twampServerConnGroup'
_Q='twampServerMIBGroup'
_P='twampServerConnectionStatus'
_O='twampServerConnPktsRecvd'
_N='twampServerConnPktsSent'
_M='twampServerConnTimeOfLastRun'
_L='twampServerConnSessionId'
_K='twampRowStatus'
_J='twampInactivityTimeout'
_I='twampPortNumber'
_H='twampServerConnClientIP'
_G='twampClientIpaddressMask'
_F='twampClientIpaddress'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='ALCATEL-IND1-TWAMP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1TWAMP,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','softentIND1TWAMP')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
alcatelIND1TWAMPMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,71,1))
if mibBuilder.loadTexts:alcatelIND1TWAMPMIB.setRevisions(('2014-10-07 00:00',))
_AlcatelIND1TWAMPMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1TWAMPMIBObjects=_AlcatelIND1TWAMPMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,71,1,1))
if mibBuilder.loadTexts:alcatelIND1TWAMPMIBObjects.setStatus(_A)
_TwampServerMIB_ObjectIdentity=ObjectIdentity
twampServerMIB=_TwampServerMIB_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,71,1,1,1))
_TwampServerTable_Object=MibTable
twampServerTable=_TwampServerTable_Object((1,3,6,1,4,1,6486,800,1,2,1,71,1,1,1,1))
if mibBuilder.loadTexts:twampServerTable.setStatus(_A)
_TwampServerTableEntry_Object=MibTableRow
twampServerTableEntry=_TwampServerTableEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,71,1,1,1,1,1))
twampServerTableEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:twampServerTableEntry.setStatus(_A)
class _TwampPortNumber_Type(Integer32):defaultValue=862;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_TwampPortNumber_Type.__name__=_E
_TwampPortNumber_Object=MibTableColumn
twampPortNumber=_TwampPortNumber_Object((1,3,6,1,4,1,6486,800,1,2,1,71,1,1,1,1,1,1),_TwampPortNumber_Type())
twampPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:twampPortNumber.setStatus(_A)
class _TwampInactivityTimeout_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_TwampInactivityTimeout_Type.__name__=_E
_TwampInactivityTimeout_Object=MibTableColumn
twampInactivityTimeout=_TwampInactivityTimeout_Object((1,3,6,1,4,1,6486,800,1,2,1,71,1,1,1,1,1,2),_TwampInactivityTimeout_Type())
twampInactivityTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:twampInactivityTimeout.setStatus(_A)
_TwampClientIpaddress_Type=IpAddress
_TwampClientIpaddress_Object=MibTableColumn
twampClientIpaddress=_TwampClientIpaddress_Object((1,3,6,1,4,1,6486,800,1,2,1,71,1,1,1,1,1,3),_TwampClientIpaddress_Type())
twampClientIpaddress.setMaxAccess(_D)
if mibBuilder.loadTexts:twampClientIpaddress.setStatus(_A)
_TwampClientIpaddressMask_Type=IpAddress
_TwampClientIpaddressMask_Object=MibTableColumn
twampClientIpaddressMask=_TwampClientIpaddressMask_Object((1,3,6,1,4,1,6486,800,1,2,1,71,1,1,1,1,1,4),_TwampClientIpaddressMask_Type())
twampClientIpaddressMask.setMaxAccess(_D)
if mibBuilder.loadTexts:twampClientIpaddressMask.setStatus(_A)
_TwampRowStatus_Type=RowStatus
_TwampRowStatus_Object=MibTableColumn
twampRowStatus=_TwampRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,71,1,1,1,1,1,5),_TwampRowStatus_Type())
twampRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:twampRowStatus.setStatus(_A)
_TwampServerConnectionTable_Object=MibTable
twampServerConnectionTable=_TwampServerConnectionTable_Object((1,3,6,1,4,1,6486,800,1,2,1,71,1,1,2))
if mibBuilder.loadTexts:twampServerConnectionTable.setStatus(_A)
_TwampServerConnectionTableEntry_Object=MibTableRow
twampServerConnectionTableEntry=_TwampServerConnectionTableEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,71,1,1,2,1))
twampServerConnectionTableEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:twampServerConnectionTableEntry.setStatus(_A)
_TwampServerConnClientIP_Type=IpAddress
_TwampServerConnClientIP_Object=MibTableColumn
twampServerConnClientIP=_TwampServerConnClientIP_Object((1,3,6,1,4,1,6486,800,1,2,1,71,1,1,2,1,1),_TwampServerConnClientIP_Type())
twampServerConnClientIP.setMaxAccess(_C)
if mibBuilder.loadTexts:twampServerConnClientIP.setStatus(_A)
_TwampServerConnSessionId_Type=SnmpAdminString
_TwampServerConnSessionId_Object=MibTableColumn
twampServerConnSessionId=_TwampServerConnSessionId_Object((1,3,6,1,4,1,6486,800,1,2,1,71,1,1,2,1,2),_TwampServerConnSessionId_Type())
twampServerConnSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:twampServerConnSessionId.setStatus(_A)
_TwampServerConnTimeOfLastRun_Type=DisplayString
_TwampServerConnTimeOfLastRun_Object=MibTableColumn
twampServerConnTimeOfLastRun=_TwampServerConnTimeOfLastRun_Object((1,3,6,1,4,1,6486,800,1,2,1,71,1,1,2,1,3),_TwampServerConnTimeOfLastRun_Type())
twampServerConnTimeOfLastRun.setMaxAccess(_C)
if mibBuilder.loadTexts:twampServerConnTimeOfLastRun.setStatus(_A)
_TwampServerConnPktsSent_Type=Integer32
_TwampServerConnPktsSent_Object=MibTableColumn
twampServerConnPktsSent=_TwampServerConnPktsSent_Object((1,3,6,1,4,1,6486,800,1,2,1,71,1,1,2,1,4),_TwampServerConnPktsSent_Type())
twampServerConnPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:twampServerConnPktsSent.setStatus(_A)
_TwampServerConnPktsRecvd_Type=Integer32
_TwampServerConnPktsRecvd_Object=MibTableColumn
twampServerConnPktsRecvd=_TwampServerConnPktsRecvd_Object((1,3,6,1,4,1,6486,800,1,2,1,71,1,1,2,1,5),_TwampServerConnPktsRecvd_Type())
twampServerConnPktsRecvd.setMaxAccess(_C)
if mibBuilder.loadTexts:twampServerConnPktsRecvd.setStatus(_A)
_TwampServerConnectionStatus_Type=DisplayString
_TwampServerConnectionStatus_Object=MibTableColumn
twampServerConnectionStatus=_TwampServerConnectionStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,71,1,1,2,1,6),_TwampServerConnectionStatus_Type())
twampServerConnectionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:twampServerConnectionStatus.setStatus(_A)
_AlcatelIND1TWAMPMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1TWAMPMIBConformance=_AlcatelIND1TWAMPMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,71,1,2))
if mibBuilder.loadTexts:alcatelIND1TWAMPMIBConformance.setStatus(_A)
_AlcatelIND1TWAMPMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1TWAMPMIBGroups=_AlcatelIND1TWAMPMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,71,1,2,1))
if mibBuilder.loadTexts:alcatelIND1TWAMPMIBGroups.setStatus(_A)
_AlcatelIND1TWAMPMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1TWAMPMIBCompliances=_AlcatelIND1TWAMPMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,71,1,2,2))
if mibBuilder.loadTexts:alcatelIND1TWAMPMIBCompliances.setStatus(_A)
twampServerMIBGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,71,1,2,1,1))
twampServerMIBGroup.setObjects(*((_B,_I),(_B,_J),(_B,_F),(_B,_G),(_B,_K)))
if mibBuilder.loadTexts:twampServerMIBGroup.setStatus(_A)
twampServerConnGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,71,1,2,1,2))
twampServerConnGroup.setObjects(*((_B,_H),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:twampServerConnGroup.setStatus(_A)
alcatelIND1TWAMPMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,71,1,2,2,1))
alcatelIND1TWAMPMIBCompliance.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:alcatelIND1TWAMPMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1TWAMPMIB':alcatelIND1TWAMPMIB,'alcatelIND1TWAMPMIBObjects':alcatelIND1TWAMPMIBObjects,'twampServerMIB':twampServerMIB,'twampServerTable':twampServerTable,'twampServerTableEntry':twampServerTableEntry,_I:twampPortNumber,_J:twampInactivityTimeout,_F:twampClientIpaddress,_G:twampClientIpaddressMask,_K:twampRowStatus,'twampServerConnectionTable':twampServerConnectionTable,'twampServerConnectionTableEntry':twampServerConnectionTableEntry,_H:twampServerConnClientIP,_L:twampServerConnSessionId,_M:twampServerConnTimeOfLastRun,_N:twampServerConnPktsSent,_O:twampServerConnPktsRecvd,_P:twampServerConnectionStatus,'alcatelIND1TWAMPMIBConformance':alcatelIND1TWAMPMIBConformance,'alcatelIND1TWAMPMIBGroups':alcatelIND1TWAMPMIBGroups,_Q:twampServerMIBGroup,_R:twampServerConnGroup,'alcatelIND1TWAMPMIBCompliances':alcatelIND1TWAMPMIBCompliances,'alcatelIND1TWAMPMIBCompliance':alcatelIND1TWAMPMIBCompliance})