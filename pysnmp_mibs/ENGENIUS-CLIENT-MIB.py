_G='clientInfoTableIndex'
_F='not-accessible'
_E='signallevelTableIndex'
_D='ENGENIUS-CLIENT-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp','TruthValue')
engeniusmesh=ModuleIdentity((1,3,6,1,4,1,14125,1))
if mibBuilder.loadTexts:engeniusmesh.setRevisions(('2007-05-02 10:00',))
_Engenius_ObjectIdentity=ObjectIdentity
engenius=_Engenius_ObjectIdentity((1,3,6,1,4,1,14125))
_NodeConfiguration_ObjectIdentity=ObjectIdentity
nodeConfiguration=_NodeConfiguration_ObjectIdentity((1,3,6,1,4,1,14125,1,2))
_NodeConfigurationSignallevel_ObjectIdentity=ObjectIdentity
nodeConfigurationSignallevel=_NodeConfigurationSignallevel_ObjectIdentity((1,3,6,1,4,1,14125,1,2,30))
class _SignallevelExecute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_SignallevelExecute_Type.__name__=_C
_SignallevelExecute_Object=MibScalar
signallevelExecute=_SignallevelExecute_Object((1,3,6,1,4,1,14125,1,2,30,1),_SignallevelExecute_Type())
signallevelExecute.setMaxAccess(_B)
if mibBuilder.loadTexts:signallevelExecute.setStatus(_A)
_SignallevelTable_Object=MibTable
signallevelTable=_SignallevelTable_Object((1,3,6,1,4,1,14125,1,2,30,2))
if mibBuilder.loadTexts:signallevelTable.setStatus(_A)
_SignallevelTableEntry_Object=MibTableRow
signallevelTableEntry=_SignallevelTableEntry_Object((1,3,6,1,4,1,14125,1,2,30,2,1))
signallevelTableEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:signallevelTableEntry.setStatus(_A)
class _SignallevelTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_SignallevelTableIndex_Type.__name__=_C
_SignallevelTableIndex_Object=MibTableColumn
signallevelTableIndex=_SignallevelTableIndex_Object((1,3,6,1,4,1,14125,1,2,30,2,1,1),_SignallevelTableIndex_Type())
signallevelTableIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:signallevelTableIndex.setStatus(_A)
_SignallevelTableSource_Type=OctetString
_SignallevelTableSource_Object=MibTableColumn
signallevelTableSource=_SignallevelTableSource_Object((1,3,6,1,4,1,14125,1,2,30,2,1,2),_SignallevelTableSource_Type())
signallevelTableSource.setMaxAccess(_B)
if mibBuilder.loadTexts:signallevelTableSource.setStatus(_A)
_SignallevelTableDestination_Type=OctetString
_SignallevelTableDestination_Object=MibTableColumn
signallevelTableDestination=_SignallevelTableDestination_Object((1,3,6,1,4,1,14125,1,2,30,2,1,3),_SignallevelTableDestination_Type())
signallevelTableDestination.setMaxAccess(_B)
if mibBuilder.loadTexts:signallevelTableDestination.setStatus(_A)
_SignallevelTableRssi_Type=OctetString
_SignallevelTableRssi_Object=MibTableColumn
signallevelTableRssi=_SignallevelTableRssi_Object((1,3,6,1,4,1,14125,1,2,30,2,1,4),_SignallevelTableRssi_Type())
signallevelTableRssi.setMaxAccess(_B)
if mibBuilder.loadTexts:signallevelTableRssi.setStatus(_A)
_ClientInfoTable_Object=MibTable
clientInfoTable=_ClientInfoTable_Object((1,3,6,1,4,1,14125,1,2,30,3))
if mibBuilder.loadTexts:clientInfoTable.setStatus(_A)
_ClientInfoTableEntry_Object=MibTableRow
clientInfoTableEntry=_ClientInfoTableEntry_Object((1,3,6,1,4,1,14125,1,2,30,3,1))
clientInfoTableEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:clientInfoTableEntry.setStatus(_A)
class _ClientInfoTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_ClientInfoTableIndex_Type.__name__=_C
_ClientInfoTableIndex_Object=MibTableColumn
clientInfoTableIndex=_ClientInfoTableIndex_Object((1,3,6,1,4,1,14125,1,2,30,3,1,1),_ClientInfoTableIndex_Type())
clientInfoTableIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:clientInfoTableIndex.setStatus(_A)
_ClientInfoTableEssid_Type=OctetString
_ClientInfoTableEssid_Object=MibTableColumn
clientInfoTableEssid=_ClientInfoTableEssid_Object((1,3,6,1,4,1,14125,1,2,30,3,1,2),_ClientInfoTableEssid_Type())
clientInfoTableEssid.setMaxAccess(_B)
if mibBuilder.loadTexts:clientInfoTableEssid.setStatus(_A)
_ClientInfoTableMac_Type=OctetString
_ClientInfoTableMac_Object=MibTableColumn
clientInfoTableMac=_ClientInfoTableMac_Object((1,3,6,1,4,1,14125,1,2,30,3,1,3),_ClientInfoTableMac_Type())
clientInfoTableMac.setMaxAccess(_B)
if mibBuilder.loadTexts:clientInfoTableMac.setStatus(_A)
_ClientInfoTableChannel_Type=OctetString
_ClientInfoTableChannel_Object=MibTableColumn
clientInfoTableChannel=_ClientInfoTableChannel_Object((1,3,6,1,4,1,14125,1,2,30,3,1,4),_ClientInfoTableChannel_Type())
clientInfoTableChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:clientInfoTableChannel.setStatus(_A)
_ClientInfoTableRate_Type=OctetString
_ClientInfoTableRate_Object=MibTableColumn
clientInfoTableRate=_ClientInfoTableRate_Object((1,3,6,1,4,1,14125,1,2,30,3,1,5),_ClientInfoTableRate_Type())
clientInfoTableRate.setMaxAccess(_B)
if mibBuilder.loadTexts:clientInfoTableRate.setStatus(_A)
_ClientInfoTableRssi_Type=OctetString
_ClientInfoTableRssi_Object=MibTableColumn
clientInfoTableRssi=_ClientInfoTableRssi_Object((1,3,6,1,4,1,14125,1,2,30,3,1,6),_ClientInfoTableRssi_Type())
clientInfoTableRssi.setMaxAccess(_B)
if mibBuilder.loadTexts:clientInfoTableRssi.setStatus(_A)
_ClientInfoTableIdletime_Type=OctetString
_ClientInfoTableIdletime_Object=MibTableColumn
clientInfoTableIdletime=_ClientInfoTableIdletime_Object((1,3,6,1,4,1,14125,1,2,30,3,1,7),_ClientInfoTableIdletime_Type())
clientInfoTableIdletime.setMaxAccess(_B)
if mibBuilder.loadTexts:clientInfoTableIdletime.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'engenius':engenius,'engeniusmesh':engeniusmesh,'nodeConfiguration':nodeConfiguration,'nodeConfigurationSignallevel':nodeConfigurationSignallevel,'signallevelExecute':signallevelExecute,'signallevelTable':signallevelTable,'signallevelTableEntry':signallevelTableEntry,_E:signallevelTableIndex,'signallevelTableSource':signallevelTableSource,'signallevelTableDestination':signallevelTableDestination,'signallevelTableRssi':signallevelTableRssi,'clientInfoTable':clientInfoTable,'clientInfoTableEntry':clientInfoTableEntry,_G:clientInfoTableIndex,'clientInfoTableEssid':clientInfoTableEssid,'clientInfoTableMac':clientInfoTableMac,'clientInfoTableChannel':clientInfoTableChannel,'clientInfoTableRate':clientInfoTableRate,'clientInfoTableRssi':clientInfoTableRssi,'clientInfoTableIdletime':clientInfoTableIdletime})