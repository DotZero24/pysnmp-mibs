_E='nbsNtpServerIpAddr'
_D='NBS-NTP-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nbsCmmcNtpGrp,=mibBuilder.importSymbols('NBS-CMMC-MIB','nbsCmmcNtpGrp')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nbsNtpMib=ModuleIdentity((1,3,6,1,4,1,629,200,9,1))
class _NbsNtpEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notSupported',1),('no',2),('yes',3)))
_NbsNtpEnable_Type.__name__=_B
_NbsNtpEnable_Object=MibScalar
nbsNtpEnable=_NbsNtpEnable_Object((1,3,6,1,4,1,629,200,9,1,1),_NbsNtpEnable_Type())
nbsNtpEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsNtpEnable.setStatus(_A)
_NbsNtpServerTableSize_Type=Integer32
_NbsNtpServerTableSize_Object=MibScalar
nbsNtpServerTableSize=_NbsNtpServerTableSize_Object((1,3,6,1,4,1,629,200,9,1,2),_NbsNtpServerTableSize_Type())
nbsNtpServerTableSize.setMaxAccess('read-only')
if mibBuilder.loadTexts:nbsNtpServerTableSize.setStatus(_A)
_NbsNtpServerTable_Object=MibTable
nbsNtpServerTable=_NbsNtpServerTable_Object((1,3,6,1,4,1,629,200,9,1,3))
if mibBuilder.loadTexts:nbsNtpServerTable.setStatus(_A)
_NbsNtpServerEntry_Object=MibTableRow
nbsNtpServerEntry=_NbsNtpServerEntry_Object((1,3,6,1,4,1,629,200,9,1,3,1))
nbsNtpServerEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:nbsNtpServerEntry.setStatus(_A)
_NbsNtpServerIpAddr_Type=IpAddress
_NbsNtpServerIpAddr_Object=MibTableColumn
nbsNtpServerIpAddr=_NbsNtpServerIpAddr_Object((1,3,6,1,4,1,629,200,9,1,3,1,1),_NbsNtpServerIpAddr_Type())
nbsNtpServerIpAddr.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:nbsNtpServerIpAddr.setStatus(_A)
class _NbsNtpServerStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('invalid',1),('active',2)))
_NbsNtpServerStatus_Type.__name__=_B
_NbsNtpServerStatus_Object=MibTableColumn
nbsNtpServerStatus=_NbsNtpServerStatus_Object((1,3,6,1,4,1,629,200,9,1,3,1,2),_NbsNtpServerStatus_Type())
nbsNtpServerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsNtpServerStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'nbsNtpMib':nbsNtpMib,'nbsNtpEnable':nbsNtpEnable,'nbsNtpServerTableSize':nbsNtpServerTableSize,'nbsNtpServerTable':nbsNtpServerTable,'nbsNtpServerEntry':nbsNtpServerEntry,_E:nbsNtpServerIpAddr,'nbsNtpServerStatus':nbsNtpServerStatus})