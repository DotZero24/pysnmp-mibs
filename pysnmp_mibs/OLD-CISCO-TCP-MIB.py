_G='tcpConnRemPort'
_F='tcpConnRemAddress'
_E='tcpConnLocalPort'
_D='tcpConnLocalAddress'
_C='read-only'
_B='TCP-MIB'
_A='deprecated'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
local,=mibBuilder.importSymbols('CISCO-SMI','local')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tcpConnLocalAddress,tcpConnLocalPort,tcpConnRemAddress,tcpConnRemPort=mibBuilder.importSymbols(_B,_D,_E,_F,_G)
_Ltcp_ObjectIdentity=ObjectIdentity
ltcp=_Ltcp_ObjectIdentity((1,3,6,1,4,1,9,2,6))
_LtcpConnTable_Object=MibTable
ltcpConnTable=_LtcpConnTable_Object((1,3,6,1,4,1,9,2,6,1))
if mibBuilder.loadTexts:ltcpConnTable.setStatus(_A)
_LtcpConnEntry_Object=MibTableRow
ltcpConnEntry=_LtcpConnEntry_Object((1,3,6,1,4,1,9,2,6,1,1))
ltcpConnEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:ltcpConnEntry.setStatus(_A)
_LoctcpConnInBytes_Type=Integer32
_LoctcpConnInBytes_Object=MibTableColumn
loctcpConnInBytes=_LoctcpConnInBytes_Object((1,3,6,1,4,1,9,2,6,1,1,1),_LoctcpConnInBytes_Type())
loctcpConnInBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:loctcpConnInBytes.setStatus(_A)
_LoctcpConnOutBytes_Type=Integer32
_LoctcpConnOutBytes_Object=MibTableColumn
loctcpConnOutBytes=_LoctcpConnOutBytes_Object((1,3,6,1,4,1,9,2,6,1,1,2),_LoctcpConnOutBytes_Type())
loctcpConnOutBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:loctcpConnOutBytes.setStatus(_A)
_LoctcpConnInPkts_Type=Integer32
_LoctcpConnInPkts_Object=MibTableColumn
loctcpConnInPkts=_LoctcpConnInPkts_Object((1,3,6,1,4,1,9,2,6,1,1,3),_LoctcpConnInPkts_Type())
loctcpConnInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:loctcpConnInPkts.setStatus(_A)
_LoctcpConnOutPkts_Type=Integer32
_LoctcpConnOutPkts_Object=MibTableColumn
loctcpConnOutPkts=_LoctcpConnOutPkts_Object((1,3,6,1,4,1,9,2,6,1,1,4),_LoctcpConnOutPkts_Type())
loctcpConnOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:loctcpConnOutPkts.setStatus(_A)
_LoctcpConnElapsed_Type=TimeTicks
_LoctcpConnElapsed_Object=MibTableColumn
loctcpConnElapsed=_LoctcpConnElapsed_Object((1,3,6,1,4,1,9,2,6,1,1,5),_LoctcpConnElapsed_Type())
loctcpConnElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:loctcpConnElapsed.setStatus(_A)
mibBuilder.exportSymbols('OLD-CISCO-TCP-MIB',**{'ltcp':ltcp,'ltcpConnTable':ltcpConnTable,'ltcpConnEntry':ltcpConnEntry,'loctcpConnInBytes':loctcpConnInBytes,'loctcpConnOutBytes':loctcpConnOutBytes,'loctcpConnInPkts':loctcpConnInPkts,'loctcpConnOutPkts':loctcpConnOutPkts,'loctcpConnElapsed':loctcpConnElapsed})