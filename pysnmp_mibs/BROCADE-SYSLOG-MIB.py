_G='brcdSysLogServerUDPPort'
_F='brcdSysLogServerAddr'
_E='brcdSysLogServerAddrType'
_D='Unsigned32'
_C='not-accessible'
_B='BROCADE-SYSLOG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
brcdSysLog,=mibBuilder.importSymbols('FOUNDRY-SN-ROOT-MIB','brcdSysLog')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
brocadeSysLogMIB=ModuleIdentity((1,3,6,1,4,1,1991,1,1,11,1))
if mibBuilder.loadTexts:brocadeSysLogMIB.setRevisions(('2011-11-04 00:00','2017-08-07 00:00'))
_BrcdSysLogGroup_ObjectIdentity=ObjectIdentity
brcdSysLogGroup=_BrcdSysLogGroup_ObjectIdentity((1,3,6,1,4,1,1991,1,1,11,1,1))
_BrcdSysLogServerTable_Object=MibTable
brcdSysLogServerTable=_BrcdSysLogServerTable_Object((1,3,6,1,4,1,1991,1,1,11,1,1,1))
if mibBuilder.loadTexts:brcdSysLogServerTable.setStatus(_A)
_BrcdSysLogServerEntry_Object=MibTableRow
brcdSysLogServerEntry=_BrcdSysLogServerEntry_Object((1,3,6,1,4,1,1991,1,1,11,1,1,1,1))
brcdSysLogServerEntry.setIndexNames((0,_B,_E),(0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:brcdSysLogServerEntry.setStatus(_A)
_BrcdSysLogServerAddrType_Type=InetAddressType
_BrcdSysLogServerAddrType_Object=MibTableColumn
brcdSysLogServerAddrType=_BrcdSysLogServerAddrType_Object((1,3,6,1,4,1,1991,1,1,11,1,1,1,1,1),_BrcdSysLogServerAddrType_Type())
brcdSysLogServerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:brcdSysLogServerAddrType.setStatus(_A)
_BrcdSysLogServerAddr_Type=InetAddress
_BrcdSysLogServerAddr_Object=MibTableColumn
brcdSysLogServerAddr=_BrcdSysLogServerAddr_Object((1,3,6,1,4,1,1991,1,1,11,1,1,1,1,2),_BrcdSysLogServerAddr_Type())
brcdSysLogServerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:brcdSysLogServerAddr.setStatus(_A)
class _BrcdSysLogServerUDPPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrcdSysLogServerUDPPort_Type.__name__=_D
_BrcdSysLogServerUDPPort_Object=MibTableColumn
brcdSysLogServerUDPPort=_BrcdSysLogServerUDPPort_Object((1,3,6,1,4,1,1991,1,1,11,1,1,1,1,3),_BrcdSysLogServerUDPPort_Type())
brcdSysLogServerUDPPort.setMaxAccess(_C)
if mibBuilder.loadTexts:brcdSysLogServerUDPPort.setStatus(_A)
_BrcdSysLogServerOutPkts_Type=Counter32
_BrcdSysLogServerOutPkts_Object=MibTableColumn
brcdSysLogServerOutPkts=_BrcdSysLogServerOutPkts_Object((1,3,6,1,4,1,1991,1,1,11,1,1,1,1,4),_BrcdSysLogServerOutPkts_Type())
brcdSysLogServerOutPkts.setMaxAccess('read-only')
if mibBuilder.loadTexts:brcdSysLogServerOutPkts.setStatus(_A)
_BrcdSysLogServerRowStatus_Type=RowStatus
_BrcdSysLogServerRowStatus_Object=MibTableColumn
brcdSysLogServerRowStatus=_BrcdSysLogServerRowStatus_Object((1,3,6,1,4,1,1991,1,1,11,1,1,1,1,5),_BrcdSysLogServerRowStatus_Type())
brcdSysLogServerRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:brcdSysLogServerRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'brocadeSysLogMIB':brocadeSysLogMIB,'brcdSysLogGroup':brcdSysLogGroup,'brcdSysLogServerTable':brcdSysLogServerTable,'brcdSysLogServerEntry':brcdSysLogServerEntry,_E:brcdSysLogServerAddrType,_F:brcdSysLogServerAddr,_G:brcdSysLogServerUDPPort,'brcdSysLogServerOutPkts':brcdSysLogServerOutPkts,'brcdSysLogServerRowStatus':brcdSysLogServerRowStatus})