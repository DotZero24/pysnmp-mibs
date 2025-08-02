_R='NotificationType'
_Q='adslPtStatus'
_P='adslPtSpeed'
_O='adslPtOutSpeed'
_N='adslPtOutPkts'
_M='adslPtOutError'
_L='adslPtOutDrop'
_K='adslPtInSpeed'
_J='adslPtInPkts'
_I='adslPtInError'
_H='adslPtInDrop'
_G='adslPtInCRC'
_F='adslProductID'
_E='adslMemLoad'
_D='adslLineUser'
_C='adslConfigAddr'
_B='adslCPULoad'
_A='FS-NMS-1705'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adslCPULoad,adslConfigAddr,adslLineUser,adslMemLoad,adslProductID,adslPtInCRC,adslPtInDrop,adslPtInError,adslPtInPkts,adslPtInSpeed,adslPtOutDrop,adslPtOutError,adslPtOutPkts,adslPtOutSpeed,adslPtSpeed,adslPtStatus=mibBuilder.importSymbols(_A,_B,_C,_D,_E,_F,_G,_H,_I,_J,_K,_L,_M,_N,_O,_P,_Q)
nms,=mibBuilder.importSymbols('FS-NMS-SMI','nms')
ifDescr,ifIndex,ifType=mibBuilder.importSymbols('IF-MIB','ifDescr','ifIndex','ifType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysUpTime,=mibBuilder.importSymbols('SNMPv2-MIB','sysUpTime')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_R,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_R,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adslConnection=NotificationType((1,3,6,1,4,1,52642,0,0))
adslConnection.setObjects(*((_A,_D),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:adslConnection.setStatus('')
adslPeriod=NotificationType((1,3,6,1,4,1,52642,0,1))
adslPeriod.setObjects(*((_A,_E),(_A,_B),(_A,_G),(_A,_Q),(_A,_P),(_A,_N),(_A,_J),(_A,_M),(_A,_I),(_A,_O),(_A,_K),(_A,_L),(_A,_H)))
if mibBuilder.loadTexts:adslPeriod.setStatus('')
mibBuilder.exportSymbols('FS-NMSTRAP-MIB',**{'adslConnection':adslConnection,'adslPeriod':adslPeriod})