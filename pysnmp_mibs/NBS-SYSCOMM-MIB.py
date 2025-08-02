_I='nbsSyscommGateAddrPrior'
_H='nbsSyscommInetAddrPrior'
_G='nbsSyscommGateAddrAdmin'
_F='nbsSyscommInetAddrAdmin'
_E='InetAddressPrefixLength'
_D='read-write'
_C='NBS-SYSCOMM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressPrefixLength=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_E)
nbs,=mibBuilder.importSymbols('NBS-MIB','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nbsSyscommMib=ModuleIdentity((1,3,6,1,4,1,629,214))
_NbsSyscommInetGrp_ObjectIdentity=ObjectIdentity
nbsSyscommInetGrp=_NbsSyscommInetGrp_ObjectIdentity((1,3,6,1,4,1,629,214,3))
if mibBuilder.loadTexts:nbsSyscommInetGrp.setStatus(_A)
_NbsSyscommInetSlaacAddr_Type=InetAddress
_NbsSyscommInetSlaacAddr_Object=MibScalar
nbsSyscommInetSlaacAddr=_NbsSyscommInetSlaacAddr_Object((1,3,6,1,4,1,629,214,3,3),_NbsSyscommInetSlaacAddr_Type())
nbsSyscommInetSlaacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSyscommInetSlaacAddr.setStatus(_A)
_NbsSyscommInetSlaacAddrPrefix_Type=InetAddressPrefixLength
_NbsSyscommInetSlaacAddrPrefix_Object=MibScalar
nbsSyscommInetSlaacAddrPrefix=_NbsSyscommInetSlaacAddrPrefix_Object((1,3,6,1,4,1,629,214,3,5),_NbsSyscommInetSlaacAddrPrefix_Type())
nbsSyscommInetSlaacAddrPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSyscommInetSlaacAddrPrefix.setStatus(_A)
_NbsSyscommInetAddrAdmin_Type=InetAddress
_NbsSyscommInetAddrAdmin_Object=MibScalar
nbsSyscommInetAddrAdmin=_NbsSyscommInetAddrAdmin_Object((1,3,6,1,4,1,629,214,3,10),_NbsSyscommInetAddrAdmin_Type())
nbsSyscommInetAddrAdmin.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsSyscommInetAddrAdmin.setStatus(_A)
_NbsSyscommInetAddrOper_Type=InetAddress
_NbsSyscommInetAddrOper_Object=MibScalar
nbsSyscommInetAddrOper=_NbsSyscommInetAddrOper_Object((1,3,6,1,4,1,629,214,3,11),_NbsSyscommInetAddrOper_Type())
nbsSyscommInetAddrOper.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSyscommInetAddrOper.setStatus(_A)
class _NbsSyscommInetAddrPrefixAdmin_Type(InetAddressPrefixLength):defaultValue=64
_NbsSyscommInetAddrPrefixAdmin_Type.__name__=_E
_NbsSyscommInetAddrPrefixAdmin_Object=MibScalar
nbsSyscommInetAddrPrefixAdmin=_NbsSyscommInetAddrPrefixAdmin_Object((1,3,6,1,4,1,629,214,3,22),_NbsSyscommInetAddrPrefixAdmin_Type())
nbsSyscommInetAddrPrefixAdmin.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsSyscommInetAddrPrefixAdmin.setStatus(_A)
_NbsSyscommInetAddrPrefixOper_Type=InetAddressPrefixLength
_NbsSyscommInetAddrPrefixOper_Object=MibScalar
nbsSyscommInetAddrPrefixOper=_NbsSyscommInetAddrPrefixOper_Object((1,3,6,1,4,1,629,214,3,23),_NbsSyscommInetAddrPrefixOper_Type())
nbsSyscommInetAddrPrefixOper.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSyscommInetAddrPrefixOper.setStatus(_A)
_NbsSyscommGateAddrAdmin_Type=InetAddress
_NbsSyscommGateAddrAdmin_Object=MibScalar
nbsSyscommGateAddrAdmin=_NbsSyscommGateAddrAdmin_Object((1,3,6,1,4,1,629,214,3,30),_NbsSyscommGateAddrAdmin_Type())
nbsSyscommGateAddrAdmin.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsSyscommGateAddrAdmin.setStatus(_A)
_NbsSyscommGateAddrOper_Type=InetAddress
_NbsSyscommGateAddrOper_Object=MibScalar
nbsSyscommGateAddrOper=_NbsSyscommGateAddrOper_Object((1,3,6,1,4,1,629,214,3,31),_NbsSyscommGateAddrOper_Type())
nbsSyscommGateAddrOper.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSyscommGateAddrOper.setStatus(_A)
_NbsSyscommEventGrp_ObjectIdentity=ObjectIdentity
nbsSyscommEventGrp=_NbsSyscommEventGrp_ObjectIdentity((1,3,6,1,4,1,629,214,100))
if mibBuilder.loadTexts:nbsSyscommEventGrp.setStatus(_A)
_NbsSyscommEvents_ObjectIdentity=ObjectIdentity
nbsSyscommEvents=_NbsSyscommEvents_ObjectIdentity((1,3,6,1,4,1,629,214,100,0))
if mibBuilder.loadTexts:nbsSyscommEvents.setStatus(_A)
_NbsSyscommInetAddrPrior_Type=InetAddress
_NbsSyscommInetAddrPrior_Object=MibScalar
nbsSyscommInetAddrPrior=_NbsSyscommInetAddrPrior_Object((1,3,6,1,4,1,629,214,100,311),_NbsSyscommInetAddrPrior_Type())
nbsSyscommInetAddrPrior.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSyscommInetAddrPrior.setStatus(_A)
_NbsSyscommGateAddrPrior_Type=InetAddress
_NbsSyscommGateAddrPrior_Object=MibScalar
nbsSyscommGateAddrPrior=_NbsSyscommGateAddrPrior_Object((1,3,6,1,4,1,629,214,100,331),_NbsSyscommGateAddrPrior_Type())
nbsSyscommGateAddrPrior.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSyscommGateAddrPrior.setStatus(_A)
nbsSyscommInetCfgChanging=NotificationType((1,3,6,1,4,1,629,214,100,0,30))
nbsSyscommInetCfgChanging.setObjects(*((_C,_F),(_C,_G)))
if mibBuilder.loadTexts:nbsSyscommInetCfgChanging.setStatus(_A)
nbsSyscommInetCfgChanged=NotificationType((1,3,6,1,4,1,629,214,100,0,31))
nbsSyscommInetCfgChanged.setObjects(*((_C,_H),(_C,_I)))
if mibBuilder.loadTexts:nbsSyscommInetCfgChanged.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'nbsSyscommMib':nbsSyscommMib,'nbsSyscommInetGrp':nbsSyscommInetGrp,'nbsSyscommInetSlaacAddr':nbsSyscommInetSlaacAddr,'nbsSyscommInetSlaacAddrPrefix':nbsSyscommInetSlaacAddrPrefix,_F:nbsSyscommInetAddrAdmin,'nbsSyscommInetAddrOper':nbsSyscommInetAddrOper,'nbsSyscommInetAddrPrefixAdmin':nbsSyscommInetAddrPrefixAdmin,'nbsSyscommInetAddrPrefixOper':nbsSyscommInetAddrPrefixOper,_G:nbsSyscommGateAddrAdmin,'nbsSyscommGateAddrOper':nbsSyscommGateAddrOper,'nbsSyscommEventGrp':nbsSyscommEventGrp,'nbsSyscommEvents':nbsSyscommEvents,'nbsSyscommInetCfgChanging':nbsSyscommInetCfgChanging,'nbsSyscommInetCfgChanged':nbsSyscommInetCfgChanged,_H:nbsSyscommInetAddrPrior,_I:nbsSyscommGateAddrPrior})