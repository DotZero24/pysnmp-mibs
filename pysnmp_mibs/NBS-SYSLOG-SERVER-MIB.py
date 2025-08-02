_G='nbsSyslogServerIndex'
_F='NBS-SYSLOG-SERVER-MIB'
_E='Unsigned32'
_D='InetAddressType'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_D)
nbs,=mibBuilder.importSymbols('NBS-MIB','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nbsSyslogServerMib=ModuleIdentity((1,3,6,1,4,1,629,206))
_NbsSyslogServerGrp_ObjectIdentity=ObjectIdentity
nbsSyslogServerGrp=_NbsSyslogServerGrp_ObjectIdentity((1,3,6,1,4,1,629,206,1))
if mibBuilder.loadTexts:nbsSyslogServerGrp.setStatus(_A)
_NbsSyslogServerTableSize_Type=Integer32
_NbsSyslogServerTableSize_Object=MibScalar
nbsSyslogServerTableSize=_NbsSyslogServerTableSize_Object((1,3,6,1,4,1,629,206,1,1),_NbsSyslogServerTableSize_Type())
nbsSyslogServerTableSize.setMaxAccess('read-only')
if mibBuilder.loadTexts:nbsSyslogServerTableSize.setStatus(_A)
_NbsSyslogServerTable_Object=MibTable
nbsSyslogServerTable=_NbsSyslogServerTable_Object((1,3,6,1,4,1,629,206,1,2))
if mibBuilder.loadTexts:nbsSyslogServerTable.setStatus(_A)
_NbsSyslogServerEntry_Object=MibTableRow
nbsSyslogServerEntry=_NbsSyslogServerEntry_Object((1,3,6,1,4,1,629,206,1,2,1))
nbsSyslogServerEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:nbsSyslogServerEntry.setStatus(_A)
class _NbsSyslogServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_NbsSyslogServerIndex_Type.__name__=_C
_NbsSyslogServerIndex_Object=MibTableColumn
nbsSyslogServerIndex=_NbsSyslogServerIndex_Object((1,3,6,1,4,1,629,206,1,2,1,1),_NbsSyslogServerIndex_Type())
nbsSyslogServerIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:nbsSyslogServerIndex.setStatus(_A)
class _NbsSyslogServerStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('invalid',1),('active',2)))
_NbsSyslogServerStatus_Type.__name__=_C
_NbsSyslogServerStatus_Object=MibTableColumn
nbsSyslogServerStatus=_NbsSyslogServerStatus_Object((1,3,6,1,4,1,629,206,1,2,1,2),_NbsSyslogServerStatus_Type())
nbsSyslogServerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSyslogServerStatus.setStatus(_A)
class _NbsSyslogServerAddressType_Type(InetAddressType):defaultValue=1
_NbsSyslogServerAddressType_Type.__name__=_D
_NbsSyslogServerAddressType_Object=MibTableColumn
nbsSyslogServerAddressType=_NbsSyslogServerAddressType_Object((1,3,6,1,4,1,629,206,1,2,1,3),_NbsSyslogServerAddressType_Type())
nbsSyslogServerAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSyslogServerAddressType.setStatus(_A)
_NbsSyslogServerAddress_Type=InetAddress
_NbsSyslogServerAddress_Object=MibTableColumn
nbsSyslogServerAddress=_NbsSyslogServerAddress_Object((1,3,6,1,4,1,629,206,1,2,1,4),_NbsSyslogServerAddress_Type())
nbsSyslogServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSyslogServerAddress.setStatus(_A)
class _NbsSyslogServerPort_Type(Unsigned32):defaultValue=514;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NbsSyslogServerPort_Type.__name__=_E
_NbsSyslogServerPort_Object=MibTableColumn
nbsSyslogServerPort=_NbsSyslogServerPort_Object((1,3,6,1,4,1,629,206,1,2,1,5),_NbsSyslogServerPort_Type())
nbsSyslogServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSyslogServerPort.setStatus(_A)
class _NbsSyslogServerLevel_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('deprecated1',1),('emerg',2),('alert',3),('crit',4),('error',5),('warning',6),('notice',7),('info',8),('debug',9)))
_NbsSyslogServerLevel_Type.__name__=_C
_NbsSyslogServerLevel_Object=MibTableColumn
nbsSyslogServerLevel=_NbsSyslogServerLevel_Object((1,3,6,1,4,1,629,206,1,2,1,6),_NbsSyslogServerLevel_Type())
nbsSyslogServerLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSyslogServerLevel.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'nbsSyslogServerMib':nbsSyslogServerMib,'nbsSyslogServerGrp':nbsSyslogServerGrp,'nbsSyslogServerTableSize':nbsSyslogServerTableSize,'nbsSyslogServerTable':nbsSyslogServerTable,'nbsSyslogServerEntry':nbsSyslogServerEntry,_G:nbsSyslogServerIndex,'nbsSyslogServerStatus':nbsSyslogServerStatus,'nbsSyslogServerAddressType':nbsSyslogServerAddressType,'nbsSyslogServerAddress':nbsSyslogServerAddress,'nbsSyslogServerPort':nbsSyslogServerPort,'nbsSyslogServerLevel':nbsSyslogServerLevel})