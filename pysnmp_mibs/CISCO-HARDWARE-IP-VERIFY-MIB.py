_I='ciscoHardwareIpVerifyMIBStatisticGroup'
_H='chivIpVerifyPacketsDropped'
_G='chivIpVerifyCheckStatus'
_F='not-accessible'
_E='chivIpVerifyCheckTypeName'
_D='chivIpVerifyCheckIpType'
_C='Integer32'
_B='CISCO-HARDWARE-IP-VERIFY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoHardwareIpVerifyMIB=ModuleIdentity((1,3,6,1,4,1,9,9,804))
if mibBuilder.loadTexts:ciscoHardwareIpVerifyMIB.setRevisions(('2012-09-04 00:00',))
_CiscoHardwareIpVerifyMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoHardwareIpVerifyMIBNotifs=_CiscoHardwareIpVerifyMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,804,0))
_CiscoHardwareIpVerifyMIBObjects_ObjectIdentity=ObjectIdentity
ciscoHardwareIpVerifyMIBObjects=_CiscoHardwareIpVerifyMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,804,1))
_ChivIpVerifyTable_Object=MibTable
chivIpVerifyTable=_ChivIpVerifyTable_Object((1,3,6,1,4,1,9,9,804,1,1))
if mibBuilder.loadTexts:chivIpVerifyTable.setStatus(_A)
_ChivIpVerifyEntry_Object=MibTableRow
chivIpVerifyEntry=_ChivIpVerifyEntry_Object((1,3,6,1,4,1,9,9,804,1,1,1))
chivIpVerifyEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:chivIpVerifyEntry.setStatus(_A)
class _ChivIpVerifyCheckIpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
_ChivIpVerifyCheckIpType_Type.__name__=_C
_ChivIpVerifyCheckIpType_Object=MibTableColumn
chivIpVerifyCheckIpType=_ChivIpVerifyCheckIpType_Object((1,3,6,1,4,1,9,9,804,1,1,1,1),_ChivIpVerifyCheckIpType_Type())
chivIpVerifyCheckIpType.setMaxAccess(_F)
if mibBuilder.loadTexts:chivIpVerifyCheckIpType.setStatus(_A)
class _ChivIpVerifyCheckTypeName_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('addressSrcBroadcast',1),('addressSrcMulticast',2),('addressDestZero',3),('addressIdentical',4),('addressSrcReserved',5),('addressClassE',6),('checksum',7),('protocol',8),('fragment',9),('lengthMinimum',10),('lengthConsistent',11),('lengthMaximumFragment',12),('lengthMaximumUdp',13),('lengthMaximumTcp',14),('tcpFlags',15),('tcpTinyFlags',16),('version',17)))
_ChivIpVerifyCheckTypeName_Type.__name__=_C
_ChivIpVerifyCheckTypeName_Object=MibTableColumn
chivIpVerifyCheckTypeName=_ChivIpVerifyCheckTypeName_Object((1,3,6,1,4,1,9,9,804,1,1,1,2),_ChivIpVerifyCheckTypeName_Type())
chivIpVerifyCheckTypeName.setMaxAccess(_F)
if mibBuilder.loadTexts:chivIpVerifyCheckTypeName.setStatus(_A)
class _ChivIpVerifyCheckStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_ChivIpVerifyCheckStatus_Type.__name__=_C
_ChivIpVerifyCheckStatus_Object=MibTableColumn
chivIpVerifyCheckStatus=_ChivIpVerifyCheckStatus_Object((1,3,6,1,4,1,9,9,804,1,1,1,3),_ChivIpVerifyCheckStatus_Type())
chivIpVerifyCheckStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:chivIpVerifyCheckStatus.setStatus(_A)
_ChivIpVerifyPacketsDropped_Type=Counter64
_ChivIpVerifyPacketsDropped_Object=MibTableColumn
chivIpVerifyPacketsDropped=_ChivIpVerifyPacketsDropped_Object((1,3,6,1,4,1,9,9,804,1,1,1,4),_ChivIpVerifyPacketsDropped_Type())
chivIpVerifyPacketsDropped.setMaxAccess('read-only')
if mibBuilder.loadTexts:chivIpVerifyPacketsDropped.setStatus(_A)
_CiscoHardwareIpVerifyMIBConform_ObjectIdentity=ObjectIdentity
ciscoHardwareIpVerifyMIBConform=_CiscoHardwareIpVerifyMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,804,2))
_CiscoHardwareIpVerifyMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoHardwareIpVerifyMIBCompliances=_CiscoHardwareIpVerifyMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,804,2,1))
_CiscoHardwareIpVerifyMIBGroups_ObjectIdentity=ObjectIdentity
ciscoHardwareIpVerifyMIBGroups=_CiscoHardwareIpVerifyMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,804,2,2))
ciscoHardwareIpVerifyMIBStatisticGroup=ObjectGroup((1,3,6,1,4,1,9,9,804,2,2,1))
ciscoHardwareIpVerifyMIBStatisticGroup.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:ciscoHardwareIpVerifyMIBStatisticGroup.setStatus(_A)
ciscoHardwareIpVerifyMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,804,2,1,1))
ciscoHardwareIpVerifyMIBCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:ciscoHardwareIpVerifyMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoHardwareIpVerifyMIB':ciscoHardwareIpVerifyMIB,'ciscoHardwareIpVerifyMIBNotifs':ciscoHardwareIpVerifyMIBNotifs,'ciscoHardwareIpVerifyMIBObjects':ciscoHardwareIpVerifyMIBObjects,'chivIpVerifyTable':chivIpVerifyTable,'chivIpVerifyEntry':chivIpVerifyEntry,_D:chivIpVerifyCheckIpType,_E:chivIpVerifyCheckTypeName,_G:chivIpVerifyCheckStatus,_H:chivIpVerifyPacketsDropped,'ciscoHardwareIpVerifyMIBConform':ciscoHardwareIpVerifyMIBConform,'ciscoHardwareIpVerifyMIBCompliances':ciscoHardwareIpVerifyMIBCompliances,'ciscoHardwareIpVerifyMIBCompliance':ciscoHardwareIpVerifyMIBCompliance,'ciscoHardwareIpVerifyMIBGroups':ciscoHardwareIpVerifyMIBGroups,_I:ciscoHardwareIpVerifyMIBStatisticGroup})